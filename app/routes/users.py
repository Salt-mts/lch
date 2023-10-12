from fastapi import APIRouter, HTTPException, Depends, status
from .. import models, schemas, oauth2
from ..database import engine, get_db
from sqlalchemy.orm import Session 
from typing import List
from ..utils import get_password_hash

models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    tags=["User"]
)



@router.get("/")
def root():
    return {"message": "Hello Userssssssssss"}

# register
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.RegResponse)
def register(user: schemas.RegisterUser, db: Session = Depends(get_db)):
    #email exist
    email_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if email_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email exist in our database")
    

    user.password = get_password_hash(user.password)
    new_uza =  models.User(**user.model_dump())
    db.add(new_uza)
    db.commit()
    db.refresh(new_uza)
    return new_uza

# get user details
@router.get("/user", status_code=status.HTTP_200_OK, response_model=schemas.PersonalResponse)
def get_personal_details(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    results =  db.query(models.Personal).filter(current_user.id == models.Personal.user_id).first()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No personal details found.")
    
    return results


#get all users
# @router.get("/users", status_code=status.HTTP_200_OK, response_model=List[schemas.UserResponse])
# def get_users(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
#     uza =  db.query(models.User).all()
#     return uza

# update basic details
@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.PersonalResponse)
def update_personal_details(user: schemas.Personal, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Personal).filter(models.Personal.user_id == current_user.id)
    
    #details exist
    details_exist = query.first()
    if details_exist:
        query.update(user.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        basic = models.Personal(user_id=current_user.id, **user.model_dump())
        db.add(basic)
        db.commit()
        db.refresh(basic)
        return basic