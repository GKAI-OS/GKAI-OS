from pydantic import BaseModel


class VehicleSpecCreate(BaseModel):

    vehicle_id: int

    key: str

    value: str



class VehicleSpecResponse(BaseModel):

    id: int

    vehicle_id: int

    key: str

    value: str


    class Config:
        from_attributes = True