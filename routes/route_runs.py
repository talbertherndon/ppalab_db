from fastapi import APIRouter, Body, HTTPException
from config.database import run_collection
from pymongo.errors import DuplicateKeyError
from fastapi.encoders import jsonable_encoder

from models.systems import RunData, RunDataUpdate
from typing import List, Dict

router = APIRouter()

# CRUD for RegressionData (now referred to as Run)
@router.post("/run", response_model=RunData)
async def create_run(run: RunData):
    try:
        # First, check if a run with this name already exists
        existing_run = run_collection.find_one({"name": run.name})
        if existing_run:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"A run with the name '{run.name}' already exists"
            )
        
        # If no existing run, proceed with insertion
        result = run_collection.insert_one(run.dict())
        created_run = run_collection.find_one({"_id": result.inserted_id})
        return created_run
    except DuplicateKeyError:
        # This catches any race condition where a duplicate might slip through
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"A run with the name '{run.name}' already exists"
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/run/{run_name}", response_model=RunData)
async def read_run(run_name: str):
    run = run_collection.find_one({"name": run_name})
    if run:
        return run
    raise HTTPException(status_code=404, detail="Run not found")

@router.get("/runs", response_model=List[RunData])
async def read_runs():
    return list(run_collection.find())

@router.patch("/run/{run_name}", response_model=RunData)
async def update_run(run_name: str, run_update: RunDataUpdate = Body(...)):
    existing_run = run_collection.find_one({"name": run_name})
    if not existing_run:
        raise HTTPException(status_code=404, detail="Run not found")

    update_data = run_update.dict(exclude_unset=True)
    
    if update_data:
        updated = run_collection.find_one_and_update(
            {"name": run_name},
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