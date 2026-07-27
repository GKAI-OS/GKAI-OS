from pydantic import BaseModel
from typing import Optional



class VehicleComparisonCreate(BaseModel):

    vehicle_id_1: int

    vehicle_id_2: int

    comparison_title: str

    winner: Optional[str] = None

    reason: Optional[str] = None

    comparison_type: Optional[str] = None



class VehicleComparisonResponse(BaseModel):

    id: int

    vehicle_id_1: int

    vehicle_id_2: int

    comparison_title: str

    winner: Optional[str]

    reason: Optional[str]

    comparison_type: Optional[str]


    class Config:
        from_attributes = True