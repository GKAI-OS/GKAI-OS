from pydantic import BaseModel


class VehicleVariantCreate(BaseModel):

    vehicle_id: int

    variant_name: str

    engine: str | None = None

    fuel_type: str | None = None

    transmission: str | None = None

    price: int | None = None

    status: bool = True



class VehicleVariantResponse(BaseModel):

    id: int

    vehicle_id: int

    variant_name: str

    engine: str | None

    fuel_type: str | None

    transmission: str | None

    price: int | None

    status: bool


    class Config:
        from_attributes = True