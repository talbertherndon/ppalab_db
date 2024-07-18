from bson import ObjectId
from datetime import datetime
from typing import List, Dict
from models.systems import Accounting

def individual_serial(accounting: Dict) -> Dict:
    return {
        "id": str(accounting["_id"]),
        "name": accounting["name"],
        "run_type": accounting["run_type"],
        "purpose": accounting["purpose"],
        "user_email": accounting["user_email"],
        "workloads": accounting["workloads"],
        "use_existing_image": accounting["use_existing_image"],
        "skuCustom": accounting.get("skuCustom", {}),
        "skuOotb": accounting.get("skuOotb", {}),
        "regressionTest": accounting.get("regressionTest", "No"),
        "configs": accounting.get("configs", {}),
        "schedule": accounting.get("schedule", "1m"),
        "start_date": accounting["start_date"].isoformat(),
        "end_date": accounting["end_date"].isoformat(),
        "type": accounting.get("type", "New")
    }

def list_serial(accountings: List[Dict]) -> List[Dict]:
    return [individual_serial(accounting) for accounting in accountings]

# Function to convert dictionary to Accounting model
def dict_to_accounting(accounting_dict: Dict) -> Accounting:
    # Convert string dates to datetime objects
    accounting_dict['start_date'] = datetime.fromisoformat(accounting_dict['start_date'])
    accounting_dict['end_date'] = datetime.fromisoformat(accounting_dict['end_date'])
    return Accounting(**accounting_dict)

# Function to convert Accounting model to dictionary
def accounting_to_dict(accounting: Accounting) -> Dict:
    accounting_dict = accounting.dict()
    accounting_dict['start_date'] = accounting_dict['start_date'].isoformat()
    accounting_dict['end_date'] = accounting_dict['end_date'].isoformat()
    return accounting_dict