from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId
from uuid import UUID, uuid4

class System(BaseModel):
    system_id: str
    tags: Optional[List[str]] = None
    vendor: Optional[str] = None
    family: Optional[str] = None
    product_name: Optional[str] = None
    system_type: Optional[str] = None
    memory_type: Optional[str] = None
    memory_size: Optional[str] = None
    memory_speed: Optional[str] = None
    qdf: Optional[str] = None
    kvm: Optional[str] = None
    kvm_port: Optional[str] = None
    power_level: Optional[str] = None
    status: Optional[str] = None
    link: Optional[str] = None
    system_category: str

        
class SystemUpdate(BaseModel):
    vendor: Optional[str] = None
    tags: Optional[List[str]] = None
    family: Optional[str] = None
    product_name: Optional[str] = None
    system_type: Optional[str] = None
    memory_type: Optional[str] = None
    memory_size: Optional[str] = None
    memory_speed: Optional[str] = None
    qdf: Optional[str] = None
    kvm: Optional[str] = None
    kvm_port: Optional[str] = None
    power_level: Optional[str] = None
    status: Optional[str] = None
    link: Optional[str] = None
    system_category: Optional[str] = None

    class Config:
        from_attributes = True
    
class Workload(BaseModel):
    Default_scenario: List[str]
    RunType: str
    Score: Dict[str, Any]
    Tools: Optional[Dict[str, Any]] = None
    WorkloadVersion: Optional[str] = None
    _id: str
    image: str
    image_path: Optional[str] = None
    iteration_number: str
    status: str

class Config(BaseModel):
    MAC: str
    _id: str
    hostname: str
    kvm: str
    lab_name: str
    status: str
    startDate: Optional[str] = None
    endDate: Optional[str] = None
    workloads: List[Workload]
    

class RunData(BaseModel):
    run_id: str
    configs: List[Config]
    maestro_link: str
    name: str = Field(..., min_length=1, max_length=100, description="Name of the run (must be unique)")
    regression: str
    regression_test: str
    purpose: Optional[str] = None
    run_date: str
    endDate: Optional[str] = None
    status: str
    user_email: str
    workloads: List[Dict[str, Any]]

class RunDataUpdate(BaseModel):
    configs: Optional[List[Config]] = None
    maestro_link: Optional[str] = None
    regression: Optional[str] = None
    regression_test: Optional[str] = None
    purpose: Optional[str] = None
    run_date: Optional[str] = None
    endDate: Optional[str] = None
    status: Optional[str] = None
    user_email: Optional[str] = None
    workloads: Optional[List[Dict[str, Any]]] = None

    class Config:
        arbitrary_types_allowed = True
        
        