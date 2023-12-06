from fastapi import APIRouter, HTTPException, Depends, status
from .. import models, schemas, oauth2
from ..database import get_db
from sqlalchemy.orm import Session 
from sqlalchemy import func, desc
from datetime import timedelta, datetime



router = APIRouter(
    tags=['subscription']
)

  

# ***************ADD SUBSCRIPTION******************
@router.post("/monthly_sub/{business_id}", status_code=status.HTTP_200_OK, response_model=schemas.Subscription)
def monthly_sub(business_id: int, db: Session = Depends(get_db)):

    query = db.query(models.Business).filter(models.Business.id == business_id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No business with id of {business_id} found")

    startdate = datetime.now()
    enddate = startdate + timedelta(days=30)

    insert = models.Subscription(business_id = business_id, start_date = startdate, end_date = enddate)
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return insert


@router.post("/yearly_sub/{business_id}", status_code=status.HTTP_200_OK, response_model=schemas.Subscription)
def yearly_sub(business_id: int, db: Session = Depends(get_db)):

    query = db.query(models.Business).filter(models.Business.id == business_id)
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No business with id of {business_id} found")

    startdate = datetime.now()
    enddate = startdate + timedelta(days=365)

    insert = models.Subscription(business_id = business_id, start_date = startdate, end_date = enddate)
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return insert


# ***************RENEW SUBSCRIPTION BEFORE EXPIRY******************
@router.post("/renew_monthly_sub/{business_id}", status_code=status.HTTP_200_OK, response_model=schemas.Subscription)
def renew_monthly_sub(business_id: int,  db: Session = Depends(get_db)):

    query = db.query(models.Subscription).filter(models.Subscription.business_id == business_id).order_by(desc(models.Subscription.id))
    if not query.first().is_active:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"No active subscription! Start a new subscription")

    startdate = query.first().end_date
    enddate = startdate + timedelta(days=30)

    insert = models.Subscription(business_id = business_id, start_date = startdate, end_date = enddate)
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return insert


@router.post("/renew_yearly_sub/{business_id}", status_code=status.HTTP_200_OK, response_model=schemas.Subscription)
def renew_yearly_sub(business_id: int,  db: Session = Depends(get_db)):

    query = db.query(models.Subscription).filter(models.Subscription.business_id == business_id).order_by(desc(models.Subscription.id))
    if not query.first().is_active:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"No active subscription! Start a new subscription")

    startdate = query.first().end_date
    enddate = startdate + timedelta(days=365)

    insert = models.Subscription(business_id = business_id, start_date = startdate, end_date = enddate)
    db.add(insert)
    db.commit()
    db.refresh(insert)
    return insert

