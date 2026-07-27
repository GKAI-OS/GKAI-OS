from pydantic import BaseModel
from typing import Optional


class VehicleSourceCreate(BaseModel):

    vehicle_id: int

    source_name: str

    source_type: str

    source_url: Optional[str] = None

    data_category: str

    verified_status: Optional[str] = "Pending"

    verified_by: Optional[str] = None

    verified_date: Optional[str] = None



class VehicleSourceResponse(BaseModel):

    id: int

    vehicle_id: int

    source_name: str

    source_type: str

    source_url: Optional[str]

    data_category: str

    verified_status: str

    verified_by: Optional[str]

    verified_date: Optional[str]


    class Config:
        from_attributes = True