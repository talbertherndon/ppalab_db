from fastapi import APIRouter, HTTPException
from schema.schema_accounting import list_serial, dict_to_accounting, individual_serial, accounting_to_dict
from config.database import accounting_collection
from models.systems import Accounting

from bson import ObjectId
from typing import List, Dict

router = APIRouter()

@router.get("/accounting", response_model=List[Accounting])
async def get_all_accounting():
    accountings = list_serial(accounting_collection.find())
    return [dict_to_accounting(acc) for acc in accountings]

@router.get("/accounting/{id}", response_model=Accounting)
async def get_accounting(id: str):
    accounting = accounting_collection.find_one({"_id": ObjectId(id)})
    if accounting:
        return dict_to_accounting(individual_serial(accounting))
    raise HTTPException(status_code=404, detail="Accounting record not found")

@router.post("/accounting", response_model=Accounting)
async def create_accounting(accounting: Accounting):
    accounting_dict = accounting_to_dict(accounting)
    result = accounting_collection.insert_one(accounting_dict)
    created_accounting = accounting_collection.find_one({"_id": result.inserted_id})
    return dict_to_accounting(individual_serial(created_accounting))

@router.put("/accounting/{id}", response_model=Accounting)
async def update_accounting(id: str, accounting: Accounting):
    accounting_dict = accounting_to_dict(accounting)
    result = accounting_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": accounting_dict},
        return_document=True
    )
    if result:
        return dict_to_accounting(individual_serial(result))
    raise HTTPException(status_code=404, detail="Accounting record not found")

@router.delete("/accounting/{id}", response_model=Dict)
async def delete_accounting(id: str):
    result = accounting_collection.find_one_and_delete({"_id": ObjectId(id)})
    if result:
        return {"message": "Accounting record deleted successfully"}
    raise HTTPException(status_code=404, detail="Accounting record not found")