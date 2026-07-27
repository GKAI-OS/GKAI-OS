from pydantic import BaseModel


class VehicleFuelCreate(BaseModel):

    vehicle_id: int

    fuel_type: str

    fuel_capacity: str | None = None

    ethanol_percentage: str | None = None

    battery_capacity: str | None = None

    range: str | None = None

    charging_type: str | None = None

    charging_time: str | None = None



class VehicleFuelResponse(BaseModel):

    id: int

    vehicle_id: int

    fuel_type: str

    fuel_capacity: str | None

    ethanol_percentage: str | None

    battery_capacity: str | None

    range: str | None

    charging_type: str | None

    charging_time: str | None


    class Config:
        from_attributes = True