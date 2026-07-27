from pydantic import BaseModel
from typing import Optional


class VehicleSafetyCreate(BaseModel):

    vehicle_id: int

    airbags: Optional[str] = None

    abs: Optional[bool] = False

    ebd: Optional[bool] = False

    traction_control: Optional[bool] = False

    hill_assist: Optional[bool] = False

    esp: Optional[bool] = False

    adas: Optional[str] = None

    safety_rating: Optional[str] = None



class VehicleSafetyResponse(BaseModel):

    id: int

    vehicle_id: int

    airbags: Optional[str] = None

    abs: bool

    ebd: bool

    traction_control: bool

    hill_assist: bool

    esp: bool

    adas: Optional[str] = None

    safety_rating: Optional[str] = None


    class Config:
        from_attributes = True