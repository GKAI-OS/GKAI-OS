from pydantic import BaseModel


class VehiclePerformanceCreate(BaseModel):

    vehicle_id: int

    engine_power: str | None = None

    torque: str | None = None

    mileage: str | None = None

    top_speed: str | None = None

    acceleration: str | None = None

    battery_range: str | None = None

    charging_time: str | None = None



class VehiclePerformanceResponse(BaseModel):

    id: int

    vehicle_id: int

    engine_power: str | None

    torque: str | None

    mileage: str | None

    top_speed: str | None

    acceleration: str | None

    battery_range: str | None

    charging_time: str | None


    class Config:
        from_attributes = True