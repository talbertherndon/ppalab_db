from fastapi import APIRouter, HTTPException

from models.systems import System
from config.database import system_collection
from schema.schema_system import individual_serial, list_serial

from typing import List
from bson import ObjectId

router = APIRouter()


# GET Request Method to fetch all systems
@router.get("/systems", response_model=List[System])
async def get_systems():
    systems = list_serial(system_collection.find())
    return systems

@router.get("/systems/{id}", response_model=System)
async def get_system(id: str):
    system = system_collection.find_one({"_id": ObjectId(id)})
    if system:
        return individual_serial(system)
    raise HTTPException(status_code=404, detail="System not found")

# POST Request Method to create a new system
@router.post("/systems", response_model=System)
async def create_system(system: System):
    new_system = system.dict(exclude={"id"})  # Convert to dict and exclude id
    result = system_collection.insert_one(new_system)
    created_system = system_collection.find_one({"_id": result.inserted_id})
    return individual_serial(created_system)

# PUT Request Method to update a system
@router.put("/systems/{id}", response_model=System)
async def update_system(id: str, system: System):
    updated_system = system.dict(exclude={"id"})  # Convert to dict and exclude id
    result = system_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": updated_system},
        return_document=True
    )
    if result:
        return individual_serial(result)
    raise HTTPException(status_code=404, detail="System not found")

# DELETE Request Method to delete a system
@router.delete("/systems/{id}", response_model=dict)
async def delete_system(id: str):
    result = system_collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"message": "System deleted successfully"}
    raise HTTPException(status_code=404, detail="System not found")