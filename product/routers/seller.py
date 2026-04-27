from fastapi import APIRouter, status
from ..import schemas
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from passlib.context import CryptContext
from ..import models
from product.routers.login import get_current_user

router = APIRouter(tags=['Seller'])

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/seller', response_model=schemas.DisplaySeller, status_code=status.HTTP_201_CREATED)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db), current_user:schemas.Seller = Depends(get_current_user)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username, email=request.email, password=hashed_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller

@router.delete('/seller/{id}')
def delete(id, db: Session = Depends(get_db), current_user:schemas.Seller = Depends(get_current_user)):
    db.query(models.Seller).filter(models.Seller.id == id).delete(synchronize_session=False)
    db.commit()
    return {f'Seller with ID {id} deleted.'}