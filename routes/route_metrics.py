from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from config.database import run_collection, system_collection, workloads_collection
from pymongo.errors import DuplicateKeyError
from fastapi.encoders import jsonable_encoder
from models.systems import System, RunData, Workload
from typing import List, Dict, Optional, Literal

import uuid

router = APIRouter()


class SystemCountFilter(BaseModel):
    system_ids: Optional[List[str]] = None
    system_category: Optional[str] = None
    vendor: Optional[str] = None
    status: Optional[str] = None
    
    

class RunCountFilter(BaseModel):
    hostnames: Optional[List[str]] = None
    status: Optional[str] = None
    regression: Optional[str] = None
    user_email: Optional[str] = None

class TimeSeriesFilter(BaseModel):
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    hostnames: Optional[List[str]] = None
    status: Optional[str] = None
    regression: Optional[str] = None
    purpose: Optional[str] = None
    group_by: Literal['yearly', 'monthly', 'daily'] = 'monthly'
    
    
@router.post("/runs/hostname/timeseries")
def get_hostname_timeseries_stats(filters: TimeSeriesFilter):
    """Get hostname stats grouped by year, month, or day with filters"""
    try:
        # Build match query based on filters
        match_query = {}
        
        if filters.start_date and filters.end_date:
            match_query["run_date"] = {
                "$gte": filters.start_date,
                "$lte": filters.end_date
            }
            
        if filters.status:
            match_query["status"] = filters.status
            
        if filters.regression:
            match_query["regression"] = filters.regression
            
        if filters.purpose:
            match_query["purpose"] = filters.purpose

        # Get unique hostnames based on filters
        hostname_pipeline = [
            {"$match": match_query} if match_query else {"$match": {}},
            {"$unwind": "$configs"}
        ]
        
        if filters.hostnames:
            hostname_pipeline.append({
                "$match": {"configs.hostname": {"$in": filters.hostnames}}
            })
            
        hostname_pipeline.extend([
            {"$group": {
                "_id": None,
                "hostnames": {"$addToSet": "$configs.hostname"}
            }}
        ])
        
        unique_hostnames = list(run_collection.aggregate(hostname_pipeline))[0]["hostnames"]
        
        # Main aggregation pipeline
        pipeline = [
            {"$match": match_query} if match_query else {"$match": {}},
            {"$unwind": "$configs"}
        ]
        
        if filters.hostnames:
            pipeline.append({
                "$match": {"configs.hostname": {"$in": filters.hostnames}}
            })

        # Extract date components directly using string operations
        pipeline.extend([
            {"$addFields": {
                "dateParts": {"$split": ["$run_date", ", "]},
            }},
            {"$addFields": {
                "monthDay": {"$arrayElemAt": ["$dateParts", 1]},
                "yearTime": {"$arrayElemAt": ["$dateParts", 2]},
            }},
            {"$addFields": {
                "monthDayParts": {"$split": ["$monthDay", " "]},
                "yearParts": {"$split": ["$yearTime", ", "]},
            }},
            {"$addFields": {
                "month": {"$arrayElemAt": ["$monthDayParts", 0]},
                "day": {"$arrayElemAt": ["$monthDayParts", 1]},
                "year": {"$arrayElemAt": ["$yearParts", 0]},
            }}
        ])

        # Add grouping based on selected period
        if filters.group_by == 'yearly':
            group_id = {
                "year": "$year",
                "hostname": "$configs.hostname"
            }
        elif filters.group_by == 'monthly':
            group_id = {
                "year": "$year",
                "month": "$month",
                "hostname": "$configs.hostname"
            }
        else:  # daily
            group_id = {
                "year": "$year",
                "month": "$month",
                "day": "$day",
                "hostname": "$configs.hostname"
            }

        pipeline.extend([
            {"$group": {
                "_id": group_id,
                "count": {"$sum": 1}
            }},
            {"$sort": {"_id.year": 1, "_id.month": 1, "_id.day": 1}}
        ])

        data = list(run_collection.aggregate(pipeline))
        
        # Format the results based on grouping
        result = []
        current_period = None
        period_entry = {}

        for item in data:
            # Format period label based on grouping
            if filters.group_by == 'yearly':
                period_key = item["_id"]["year"]
            elif filters.group_by == 'monthly':
                period_key = f"{item['_id']['month']} {item['_id']['year']}"
            else:  # daily
                period_key = f"{item['_id']['month']} {item['_id']['day']}, {item['_id']['year']}"

            if period_key != current_period:
                if current_period is not None:
                    result.append(period_entry)
                current_period = period_key
                period_entry = {"period": period_key}
                
                # Initialize all hostnames with 0
                for hostname in unique_hostnames:
                    period_entry[hostname] = 0
            
            hostname = item["_id"]["hostname"]
            period_entry[hostname] = item["count"]

        # Append the last period entry
        if period_entry:
            result.append(period_entry)

        # Create ordered period entries with sorted hostname counts
        ordered_result = []
        for entry in result:
            # Create list of (hostname, count) tuples, excluding 'period'
            items = [(k, v) for k, v in entry.items() if k != 'period']
            # Sort by count in descending order
            items.sort(key=lambda x: x[1], reverse=True)
            
            # Create new ordered dictionary starting with 'period'
            ordered_entry = {"period": entry["period"]}
            # Add sorted hostname-count pairs
            for hostname, count in items:
                ordered_entry[hostname] = count
                
            ordered_result.append(ordered_entry)
        
        series = [
            {
                "dataKey": hostname,
                "label": hostname,
            }
            for hostname in unique_hostnames
        ]

        return {
            "data": ordered_result,
            "filters_applied": filters.dict(exclude_none=True),
            "hostnames": unique_hostnames,
            "series": series
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error getting hostname stats: {str(e)}"
        )
    
@router.post("/configs/count/filtered")
async def get_filtered_configs_count(filter_params: RunCountFilter):
    """Get total configs count based on filter criteria"""
    try:
        pipeline = []
        match_query = {}
        
        # Build match query for filtering
        if filter_params.hostnames:
            match_query["configs.hostname"] = {"$in": filter_params.hostnames}
        
        if filter_params.status:
            match_query["status"] = filter_params.status
            
        if filter_params.regression:
            match_query["regression"] = filter_params.regression
            
        if filter_params.user_email:
            match_query["user_email"] = filter_params.user_email

        # Add match stage if there are any filters
        if match_query:
            pipeline.append({"$match": match_query})

        # Unwind the configs array to count individual configs
        pipeline.append({"$unwind": "$configs"})

        # Add additional hostname filter after unwind if needed
        if filter_params.hostnames:
            pipeline.append({
                "$match": {
                    "configs.hostname": {"$in": filter_params.hostnames}
                }
            })

        # Count the total configs
        pipeline.append({
            "$count": "total_configs"
        })

        # Execute aggregation
        result = list(run_collection.aggregate(pipeline))
        
        total_configs = result[0]["total_configs"] if result else 0
        
        return {
            "total_configs": total_configs,
            "filters_applied": {k: v for k, v in filter_params.dict().items() if v is not None}
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error getting filtered configs count: {str(e)}"
        )

@router.post("/runs/purpose/count")
def get_runs_by_purpose(filter_params: RunCountFilter):
    """Get runs count grouped by purpose in specified format"""
    try:
        pipeline = []
        match_query = {}
        
        # Build match query for filtering
        if filter_params.hostnames:
            match_query["configs.hostname"] = {"$in": filter_params.hostnames}
        
        if filter_params.status:
            match_query["status"] = filter_params.status
            
        if filter_params.regression:
            match_query["regression"] = filter_params.regression
            
        if filter_params.user_email:
            match_query["user_email"] = filter_params.user_email

        # Add match stage if there are any filters
        if match_query:
            pipeline.append({"$match": match_query})

        # Group by purpose and count
        pipeline.append({
            "$group": {
                "_id": {
                    "$ifNull": ["$purpose", "No Purpose"]  # Handle null purposes
                },
                "count": {"$sum": 1}
            }
        })

        # Sort by count descending
        pipeline.append({"$sort": {"count": -1}})

        # Project to match desired format
        pipeline.append({
            "$project": {
                "_id": 0,
                "id": {"$toString": "$_id"},  # Convert _id to string
                "value": "$count",
                "label": "$_id"
            }
        })

        # Execute aggregation
        result = list(run_collection.aggregate(pipeline))
        
        # Add index-based ids if needed
        for i, item in enumerate(result):
            item["id"] = i

        return {
            "data": result,
            "filters_applied": {k: v for k, v in filter_params.dict().items() if v is not None}
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error getting runs by purpose: {str(e)}"
        )
            
@router.post("/runs/count/filtered")
async def get_filtered_runs_count(filter_params: RunCountFilter):
    """Get runs count based on filter criteria, including hostname filters"""
    try:
        query = {}
        
        # Filter by hostnames in configs array
        if filter_params.hostnames:
            query["configs"] = {
                "$elemMatch": {
                    "hostname": {"$in": filter_params.hostnames}
                }
            }
        
        if filter_params.status:
            query["status"] = filter_params.status
            
        if filter_params.regression:
            query["regression"] = filter_params.regression
            
        if filter_params.user_email:
            query["user_email"] = filter_params.user_email

        filtered_count = run_collection.count_documents(query)
        return {
            "filtered_count": filtered_count,
            "filters_applied": {k: v for k, v in filter_params.dict().items() if v is not None}
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Error getting filtered runs count: {str(e)}"
        )