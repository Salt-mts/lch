from fastapi import APIRouter, HTTPException, Depends, status
from .. import models, schemas
from ..database import engine, get_db
from sqlalchemy.orm import Session 
from typing import List

router = APIRouter(
    tags=['category']
)

# ***************ADD CATEGORY*******************
@router.post("/category", status_code=status.HTTP_201_CREATED)
def add_category(cat: schemas.Category, db: Session = Depends(get_db)):

    insert = models.Category( **cat.model_dump())
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return insert


# ***************DELETE CATEGORY*******************
@router.delete("/category/{id}", status_code=status.HTTP_200_OK)
def delete_category(id: int, db: Session = Depends(get_db)):
    stmt = db.query(models.Category).filter(models.Category.id == id)
    if stmt.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'not found')
    
    stmt.delete(synchronize_session=False)
    db.commit()


# ***************GET CATEGORY*******************
@router.get("/category", status_code=status.HTTP_200_OK, response_model=List[schemas.CategoryResponse])
def get_category(db: Session = Depends(get_db)):
    category = db.query(models.Category).all()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No category found!")
    return category