from fastapi import APIRouter, Body, HTTPException
from config.database import run_collection
from pymongo.errors import DuplicateKeyError
from fastapi.encoders import jsonable_encoder

from models.systems import RunData, RunDataUpdate
from typing import List, Dict

import uuid

router = APIRouter()

# CRUD for RegressionData (now referred to as Run)
@router.post("/run", response_model=RunData)
async def create_run(run: RunData):
    # If no existing run, proceed with insertion
    new_run = run.dict(exclude={"id","run_id"}, exclude_unset=True)
    new_run["run_id"] = str(uuid.uuid4())
    
    result = run_collection.insert_one(new_run)
    created_run = run_collection.find_one({"_id": result.inserted_id})
    return created_run

@router.get("/run/{id}", response_model=RunData)
async def read_run(id: str):
    run = run_collection.find_one({"run_id": id})
    if run:
        return run
    raise HTTPException(status_code=404, detail="Run not found")

@router.get("/runs", response_model=List[RunData])
async def read_runs():
    return list(run_collection.find())

@router.get("/runs_by_email/{email}", response_model=List[RunData])
async def read_runs_by_user(email: str):
    return list(run_collection.find({"user_email":email}))

@router.get("/runs_by_system/{system}", response_model=List[RunData])
async def read_runs_by_system(system: str):
    runs = list(run_collection.find())
    filtered_runs = []
    
    for run in runs:
        # Check if configs exists and is not empty
        if "configs" in run and run["configs"]:
            # Look for matching hostname in configs array
            for config in run["configs"]:
                if config.get("hostname") == system:
                    filtered_runs.append(run)
                    break  # Break once we find a match in this run's configs
    
    return filtered_runs

@router.patch("/run/{run_id}", response_model=RunData)
async def update_run(run_id: str, run_update: RunDataUpdate = Body(...)):
    existing_run = run_collection.find_one({"run_id": run_id})
    if not existing_run:
        raise HTTPException(status_code=404, detail="Run not found")

    update_data = run_update.dict(exclude_unset=True)
    
    if update_data:
        updated = run_collection.find_one_and_update(
            {"run_id": run_id},
            {"$set": jsonable_encoder(update_data)},
            return_document=True
        )
        return RunData(**updated)
    
    return RunData(**existing_run)

# @router.delete("/run/{run_name}")
# async def delete_run(run_name: str):
#     deleted = run_collection.find_one_and_delete({"name": run_name})
#     if deleted:
#         return {"message": "Run deleted successfully"}
#     raise HTTPException(status_code=404, detail="Run not found")