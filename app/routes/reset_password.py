from fastapi import APIRouter, HTTPException, Depends, status
from .. import models, schemas, oauth2_shorttime
from ..database import get_db
from sqlalchemy.orm import Session 
from ..utils import  baseURL, get_password_hash
# from ..email import pass_reset_email

router = APIRouter(
    tags=["ResetPassword"]
)


# ***************RESET PASSWORD*******************
@router.post("/resetpassword/")
async def reset_password(email: schemas.ResetPassword, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.email == email.email)
    if query.first():
        access_token = oauth2_shorttime.create_access_token(data = {"user_id": query.first().id})
        reset_link = f"{baseURL}passwordverify/{access_token}"

        #send email
        # await pass_reset_email("Password reset", email.email, {
        #     "token": reset_link,
        #     "baseURL": baseURL,
        #     "name": query.first().firstname
        # } )

        return {"link", access_token}
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Email not found!")



# ***************RESET PASSWORD*******************
@router.put("/passwordverify/{access_token}")
def create_password(access_token: str, newpass: schemas.VerifyResetPassword, db: Session = Depends(get_db)):

    #verify token and get user
    user = oauth2_shorttime.get_current_user(db, access_token)
    
    # check if password match
    if(newpass.password != newpass.confirm_password):
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f"Passwords doesn't match")
    
    #check if user is in the database
    query = db.query(models.User).filter(models.User.id == user.id)
    if query.first():
        npass = get_password_hash(newpass.password)
        query.first().password = npass
        db.commit()
        return {"data":"success"}