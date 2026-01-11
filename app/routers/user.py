from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas, utils

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed = utils.hash(user.password)
    user.password = hashed
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
