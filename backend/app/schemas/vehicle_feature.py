from pydantic import BaseModel


class VehicleFeatureCreate(BaseModel):

    vehicle_id: int

    feature: str



class VehicleFeatureResponse(BaseModel):

    id: int

    vehicle_id: int

    feature: str


    class Config:
        from_attributes = True