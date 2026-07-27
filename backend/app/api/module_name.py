from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.module_name import ModuleName

from app.schemas.module_name import (
    ModuleNameCreate,
    ModuleNameResponse
)


router = APIRouter(
    prefix="/module-names",
    tags=["Module Names"]
)



@router.get(
    "/",
    response_model=list[ModuleNameResponse]
)
def get_module_names(
    db: Session = Depends(get_db)
):

    return db.query(ModuleName).all()



@router.post(
    "/",
    response_model=ModuleNameResponse
)
def create_module_name(
    data: ModuleNameCreate,
    db: Session = Depends(get_db)
):

    module = ModuleName(
        **data.model_dump()
    )


    db.add(module)

    db.commit()

    db.refresh(module)


    return module