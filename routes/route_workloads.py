from fastapi import APIRouter, HTTPException
from config.database import workloads_collection

from models.systems import Workload
from typing import List, Dict


router = APIRouter()
# Create
@router.post("/workloads", response_model=Workload)
async def create_workload(workload: Workload):
    workload_dict = workload.dict()
    result = workloads_collection.insert_one(workload_dict)
    created_workload = workloads_collection.find_one({"_id": result.inserted_id})
    return Workload(**created_workload)

# Read (Get all)
@router.get("/workloads", response_model=List[Workload])
async def read_workloads():
    workloads = list(workloads_collection.find())
    return [Workload(**workload) for workload in workloads]

# Read (Get one)
@router.get("/workloads/{workload_id}", response_model=Workload)
async def read_workload(workload_id: str):
    workload = workloads_collection.find_one({"_id": workload_id})
    if workload:
        return Workload(**workload)
    raise HTTPException(status_code=404, detail="Workload not found")

# Update
@router.put("/workloads/{workload_id}", response_model=Workload)
async def update_workload(workload_id: str, workload: Workload):
    update_data = workload.dict(exclude_unset=True)
    result = workloads_collection.find_one_and_update(
        {"_id": workload_id},
        {"$set": update_data},
        return_document=True
    )
    if result:
        return Workload(**result)
    raise HTTPException(status_code=404, detail="Workload not found")

# # Delete
# @router.delete("/workloads/{workload_id}")
# async def delete_workload(workload_id: str):
#     result = workloads_collection.delete_one({"_id": workload_id})
#     if result.deleted_count:
#         return {"message": "Workload deleted successfully"}
#     raise HTTPException(status_code=404, detail="Workload not found")