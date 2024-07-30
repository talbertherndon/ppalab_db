from fastapi import APIRouter, HTTPException
from config.database import run_collection

from models.systems import RunData
from typing import List, Dict

router = APIRouter()

# CRUD for RegressionData (now referred to as Run)
@router.post("/run", response_model=RunData)
async def create_run(run: RunData):
    result = run_collection.insert_one(run.dict())
    created_run = run_collection.find_one({"_id": result.inserted_id})
    return created_run

@router.get("/run/{run_name}", response_model=RunData)
async def read_run(run_name: str):
    run = run_collection.find_one({"name": run_name})
    if run:
        return run
    raise HTTPException(status_code=404, detail="Run not found")

@router.get("/runs", response_model=List[RunData])
async def read_runs():
    return list(run_collection.find())

@router.put("/run/{run_name}", response_model=RunData)
async def update_run(run_name: str, run: RunData):
    updated = run_collection.find_one_and_update(
        {"name": run_name},
        {"$set": run.dict()},
        return_document=True
    )
    if updated:
        return updated
    raise HTTPException(status_code=404, detail="Run not found")

# @router.delete("/run/{run_name}")
# async def delete_run(run_name: str):
#     deleted = run_collection.find_one_and_delete({"name": run_name})
#     if deleted:
#         return {"message": "Run deleted successfully"}
#     raise HTTPException(status_code=404, detail="Run not found")