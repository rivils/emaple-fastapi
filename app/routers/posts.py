from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import database, models, schemas, oauth2

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(database.get_db)):
    return db.query(models.Post).all()

@router.post("/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate,
                db: Session = Depends(database.get_db),
                user=Depends(oauth2.get_current_user)):
    new_post = models.Post(owner_id=user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
