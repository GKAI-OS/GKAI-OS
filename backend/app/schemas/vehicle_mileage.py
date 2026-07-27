from pydantic import BaseModel
from typing import Optional


class VehicleMileageCreate(BaseModel):

    vehicle_id: int

    fuel_type: Optional[str] = None

    city_mileage: Optional[str] = None

    highway_mileage: Optional[str] = None

    claimed_mileage: Optional[str] = None

    real_world_mileage: Optional[str] = None

    battery_range: Optional[str] = None

    efficiency: Optional[str] = None



class VehicleMileageResponse(BaseModel):

    id: int

    vehicle_id: int

    fuel_type: Optional[str]

    city_mileage: Optional[str]

    highway_mileage: Optional[str]

    claimed_mileage: Optional[str]

    real_world_mileage: Optional[str]

    battery_range: Optional[str]

    efficiency: Optional[str]


    class Config:
        from_attributes = True