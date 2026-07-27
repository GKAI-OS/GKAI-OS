from pydantic import BaseModel


class VehicleImageCreate(BaseModel):

    vehicle_id: int

    image: str



class VehicleImageResponse(BaseModel):

    id: int

    vehicle_id: int

    image: str


    class Config:
        from_attributes = True