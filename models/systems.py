from typing import List, Dict, Optional
from pydantic import BaseModel
from datetime import datetime

class System(BaseModel):
    id: str
    vendor: str
    family: str
    product_name: str
    system_type: str
    memory_type: str
    memory_size: int
    memory_speed: str
    qdf: Optional[str]
    kvm: str
    kvm_port: Optional[int]
    power_level: int
    status: str
    link: str

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
    
    