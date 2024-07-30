from typing import List, Optional, Dict, Any
from pydantic import BaseModel
from datetime import datetime

class System(BaseModel):
    id: str
    vendor: str
    family: str
    product_name: str
    system_type: str
    memory_type: str
    memory_size: str
    memory_speed: str
    qdf: Optional[str]
    kvm: str
    kvm_port: Optional[str]
    power_level: str
    status: str
    link: str
    system_category: str

    class Config:
        from_attributes = True
        



class Accounting(BaseModel):
    id: str
    name: str
    run_type: str
    purpose: str
    user_email: str
    workloads: List[str]
    use_existing_image: str
    skuCustom: Dict = {}
    skuOotb: Dict = {}
    regressionTest: str = "No"
    configs: Dict = {}
    schedule: str = "1m"
    start_date: datetime
    end_date: datetime
    type: str = "New"
    
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
    workloads: List[Workload]

class RunData(BaseModel):
    configs: List[Config]
    maestro_link: str
    name: str
    regression: str
    regression_test: str
    purpose: Optional[str] = None
    run_date: str
    end_date: Optional[str] = None
    status: str
    user_email: str
    workloads: List[Dict[str, Any]]