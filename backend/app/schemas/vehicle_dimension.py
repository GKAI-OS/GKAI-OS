from pydantic import BaseModel
from typing import Optional


class VehicleDimensionCreate(BaseModel):

    vehicle_id: int

    length: Optional[str] = None

    width: Optional[str] = None

    height: Optional[str] = None

    wheelbase: Optional[str] = None

    ground_clearance: Optional[str] = None

    boot_space: Optional[str] = None

    kerb_weight: Optional[str] = None

    seating_capacity: Optional[str] = None



class VehicleDimensionResponse(BaseModel):

    id: int

    vehicle_id: int

    length: Optional[str]

    width: Optional[str]

    height: Optional[str]

    wheelbase: Optional[str]

    ground_clearance: Optional[str]

    boot_space: Optional[str]

    kerb_weight: Optional[str]

    seating_capacity: Optional[str]


    class Config:
        from_attributes = True