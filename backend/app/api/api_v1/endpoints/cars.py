from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Car])
def get_cars(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Retrieve cars.
    """
    cars = crud.car.get_all(db)
    return cars


@router.get("/{id}", response_model=schemas.Car)
def get_car(
    id: int,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_user),
) -> Any:
    """
    Get car by ID.
    """
    car = crud.car.get(db=db, _id=id)
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    return car


@router.delete("/{id}", response_model=schemas.Car)
def delete_car(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Delete a car.
    """
    car = crud.car.get(db=db, _id=id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    if not crud.user.is_admin(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    car = crud.car.remove(db=db, _id=id)
    return car


@router.post("/", response_model=schemas.Car)
def create_car(
    *,
    db: Session = Depends(deps.get_db),
    car_create_dto: schemas.CarCreateDto,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Create new car.
    """
    if not crud.user.is_admin(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    car = crud.car.create(db=db, obj_in=car_create_dto)
    return car


@router.put("/{id}", response_model=schemas.Car)
def update_car(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    car_update_dto: schemas.CarUpdateDto,
    current_user: models.User = Depends(deps.get_current_active_admin),
) -> Any:
    """
    Update a car.
    """
    car = crud.car.get(db=db, _id=id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    if not crud.user.is_admin(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")

    car = crud.car.update(db=db, db_obj=car, obj_in=car_update_dto)
    return car
