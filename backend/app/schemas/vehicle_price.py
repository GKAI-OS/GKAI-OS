from pydantic import BaseModel


class VehiclePriceCreate(BaseModel):

    vehicle_id: int

    ex_showroom_price: int | None = None

    on_road_price: int | None = None

    insurance: int | None = None

    registration_charge: int | None = None

    discount: int | None = None

    emi: int | None = None

    notes: str | None = None



class VehiclePriceResponse(BaseModel):

    id: int

    vehicle_id: int

    ex_showroom_price: int | None

    on_road_price: int | None

    insurance: int | None

    registration_charge: int | None

    discount: int | None

    emi: int | None

    notes: str | None


    class Config:
        from_attributes = True