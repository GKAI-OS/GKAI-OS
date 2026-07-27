from pydantic import BaseModel
from typing import Optional


class VehicleColorCreate(BaseModel):

    vehicle_id: int

    color_name: str

    color_code: Optional[str] = None

    image: Optional[str] = None

    availability: Optional[str] = None



class VehicleColorResponse(BaseModel):

    id: int

    vehicle_id: int

    color_name: str

    color_code: Optional[str]

    image: Optional[str]

    availability: Optional[str]


    class Config:
        from_attributes = True