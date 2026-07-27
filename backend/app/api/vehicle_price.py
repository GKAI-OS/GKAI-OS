from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database import get_db

from app.models.vehicle_price import VehiclePrice

from app.schemas.vehicle_price import (
    VehiclePriceCreate,
    VehiclePriceResponse
)



router = APIRouter(
    prefix="/vehicle-prices",
    tags=["Vehicle Prices"]
)



# GET ALL

@router.get("/", response_model=list[VehiclePriceResponse])
def get_vehicle_prices(
    db: Session = Depends(get_db)
):

    return db.query(VehiclePrice).all()




# CREATE

@router.post("/", response_model=VehiclePriceResponse)
def create_vehicle_price(
    price: VehiclePriceCreate,
    db: Session = Depends(get_db)
):

    new_price = VehiclePrice(

        vehicle_id=price.vehicle_id,

        ex_showroom_price=price.ex_showroom_price,

        on_road_price=price.on_road_price,

        insurance=price.insurance,

        registration_charge=price.registration_charge,

        discount=price.discount,

        emi=price.emi,

        notes=price.notes
    )


    db.add(new_price)

    db.commit()

    db.refresh(new_price)


    return new_price





# GET SINGLE

@router.get("/{price_id}", response_model=VehiclePriceResponse)
def get_vehicle_price(
    price_id: int,
    db: Session = Depends(get_db)
):

    price = db.query(VehiclePrice).filter(
        VehiclePrice.id == price_id
    ).first()


    if not price:

        raise HTTPException(
            status_code=404,
            detail="Vehicle price not found"
        )


    return price





# UPDATE

@router.put("/{price_id}", response_model=VehiclePriceResponse)
def update_vehicle_price(
    price_id: int,
    price_data: VehiclePriceCreate,
    db: Session = Depends(get_db)
):

    price = db.query(VehiclePrice).filter(
        VehiclePrice.id == price_id
    ).first()


    if not price:

        raise HTTPException(
            status_code=404,
            detail="Vehicle price not found"
        )



    price.vehicle_id = price_data.vehicle_id

    price.ex_showroom_price = price_data.ex_showroom_price

    price.on_road_price = price_data.on_road_price

    price.insurance = price_data.insurance

    price.registration_charge = price_data.registration_charge

    price.discount = price_data.discount

    price.emi = price_data.emi

    price.notes = price_data.notes



    db.commit()

    db.refresh(price)


    return price






# DELETE

@router.delete("/{price_id}")
def delete_vehicle_price(
    price_id: int,
    db: Session = Depends(get_db)
):

    price = db.query(VehiclePrice).filter(
        VehiclePrice.id == price_id
    ).first()


    if not price:

        raise HTTPException(
            status_code=404,
            detail="Vehicle price not found"
        )



    db.delete(price)

    db.commit()


    return {
        "message": "Vehicle price deleted successfully"
    }