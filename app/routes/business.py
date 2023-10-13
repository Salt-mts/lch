from fastapi import APIRouter, HTTPException, Depends, status
from .. import models, schemas, oauth2
from ..database import engine, get_db
from sqlalchemy.orm import Session 

models.Base.metadata.create_all(bind=engine)


router = APIRouter(
    tags=['business']
)

# ***************ADD/UPDATE BUSINESS NAME/ABOUT*******************
@router.post("/business", status_code=status.HTTP_201_CREATED, response_model=schemas.Business)
def add_business(biz: schemas.BusinessAbout, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):

    query = db.query(models.Business).filter(models.Business.owner_id == current_user.id)

    #details exist
    details_exist = query.first()
    if details_exist:
        query.update(biz.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        # insert = models.Business(owner_id = current_user.id, name = biz.name, about = biz.about)
        insert = models.Business(owner_id = current_user.id, **biz.model_dump())
        db.add(insert)
        db.commit()
        db.refresh(insert)
        return insert
    

# ***************ADD/UPDATE EXPERIENCE*******************
@router.post("/business/experience", status_code = status.HTTP_201_CREATED, response_model=schemas.Business)
def update_experience(biz: schemas.BusinessExperience, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Business).filter(models.Business.owner_id == current_user.id)

    biz_exist = query.first()
    if biz_exist:
        query.update(biz.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Business not found, create a business first")
    

# ***************ADD/UPDATE ADDRESS*******************
@router.post("/business/address", status_code = status.HTTP_201_CREATED, response_model=schemas.Business)
def update_address(biz: schemas.BusinessAddress, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Business).filter(models.Business.owner_id == current_user.id)

    biz_exist = query.first()
    if biz_exist:
        query.update(biz.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Business not found, create a business first")
    


# ***************ADD/UPDATE WORKING DAYS AND TIME*******************
@router.post("/business/schedule", status_code = status.HTTP_201_CREATED, response_model=schemas.Business)
def update_schedule(biz: schemas.BusinessHour, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Business).filter(models.Business.owner_id == current_user.id)

    biz_exist = query.first()
    if biz_exist:
        query.update(biz.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Business not found, create a business first")
    


# ***************ADD/UPDATE SOCIAL HANDLES*******************
@router.post("/business/social", status_code = status.HTTP_201_CREATED, response_model=schemas.Business)
def update_social_media(biz: schemas.BusinessSocial, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.Business).filter(models.Business.owner_id == current_user.id)

    biz_exist = query.first()
    if biz_exist:
        query.update(biz.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Business not found, create a business first")
    

@router.get("/business", status_code=status.HTTP_200_OK, response_model=schemas.Business)
def get_personal_details(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    results =  db.query(models.Business).filter(current_user.id == models.Business.owner_id).first()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Business no found, create a business.")
    
    return results
