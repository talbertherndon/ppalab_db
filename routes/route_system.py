from fastapi import APIRouter, HTTPException

from models.systems import System, SystemUpdate
from config.database import system_collection
from fastapi.encoders import jsonable_encoder

from typing import List
from bson import ObjectId

router = APIRouter()



# GET Request Method to fetch all systems
@router.get("/systems", response_model=List[System])
async def get_systems():
    systems = list(system_collection.find())
    return [System (**system) for system in systems]

@router.get("/systems/{id}", response_model=System)
async def get_system(id: str):
    system = system_collection.find_one({"_id": ObjectId(id)})
    if system:
        return System(**system)
    raise HTTPException(status_code=404, detail="System not found")

# POST Request Method to create a new system
@router.post("/systems", response_model=System)
async def create_system(system: System):
    new_system = system.dict(exclude={"id","system_id"}, exclude_unset=True)  # Convert to dict and exclude id
    system_count = system_collection.count_documents({})
    new_system["system_id"] = str(system_count + 1)
    print(new_system)
    result = system_collection.insert_one(new_system)
    
    created_system = system_collection.find_one({"_id": result.inserted_id})
    
    if created_system is None:
        raise HTTPException(status_code=404, detail="System not found after creation")
    
    
    return System(**created_system)

#PATCH Request Method to update a system
@router.patch("/systems/{id}", response_model=System)
async def update_system(id: str, system_update: SystemUpdate):
    # Find the existing system
    existing_system = system_collection.find_one({"system_id": id})
    if not existing_system:
        raise HTTPException(status_code=404, detail="System not found")

    # Get the fields to update
    update_data = system_update.dict(exclude_unset=True)

    # Only update if there are fields to update
    if update_data:
        updated_system = system_collection.find_one_and_update(
            {"system_id": id},
            {"$set": jsonable_encoder(update_data)},
            return_document=True
        )
        if updated_system:
            return System(**updated_system)
    
    # If no updates were made, return the existing system
    return System(**existing_system)

# DELETE Request Method to delete a system
@router.delete("/systems/{id}", response_model=dict)
async def delete_system(id: str):
    result = system_collection.find_one_and_delete({"system_id": id})
    if result:
        return {"message": "System deleted successfully"}
    raise HTTPException(status_code=404, detail="System not found")