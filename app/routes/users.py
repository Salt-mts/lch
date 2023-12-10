from fastapi import APIRouter, HTTPException, Depends, status, UploadFile
from .. import models, schemas, oauth2
from ..database import engine, get_db
from sqlalchemy.orm import Session 
from ..utils import get_password_hash, verify_password, baseURL, generate_unique_id
from fastapi.responses import JSONResponse
import shutil
import os
import uuid
from ..email import welcome_email
import random

router = APIRouter(
    tags=["User"]
)



@router.get("/")
def root():
    return {"message": "Hello Userssssssssss"}

# ***************REGISTER USER******************
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=schemas.RegResponse)
async def register(user: schemas.RegisterUser, db: Session = Depends(get_db)):
    user.email = user.email.lower()
    #email exist
    email_exist = db.query(models.User).filter(models.User.email == user.email).first()
    if email_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email exist in our database")
    
    verification_code = random.randint(100000, 999999)
    fake_code = generate_unique_id(25)
    user.password = get_password_hash(user.password)

    new_uza =  models.User(verification_code = verification_code, **user.model_dump())
    db.add(new_uza)
    db.commit()
    db.refresh(new_uza)

    # send welcome email
    await welcome_email("Email Confirmation", user.email, {
        "token": f"{baseURL}register/{user.email}/{verification_code}/{fake_code}",
        "baseURL": baseURL
    } )
    return new_uza


# ***************EMAIL CONFIRMATION******************
@router.get("/register/{email}/{verify}/{code}", status_code=status.HTTP_201_CREATED)
def verify_email(email: str, verify: int, db: Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.email == email, models.User.verification_code == verify)

    # if email and code not found
    if not query.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Verification failed! Email not found, or already verified.")

    # if email and code is found
    if query.first():
        query.first().verification_code = 100001
        query.first().email_verified = 1
        db.commit()
        return {"data":"success"}



# ***************PERSONAL DETAILS*******************
@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def update_personal_details(user: schemas.Personal, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.User).filter(models.User.id == current_user.id)
    
    #details exist
    details_exist = query.first()
    if details_exist:
        query.update(user.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    


# ***************UPDATE PASSWORD*******************
@router.post("/user/password", status_code=status.HTTP_202_ACCEPTED)
def update_password(user: schemas.Password, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):

    user.password = get_password_hash(user.password)

    query = db.query(models.User).filter(models.User.id == current_user.id)
    
    #user exist
    user_exist = query.first()
    if user_exist:
        verfy_pass = verify_password(user.old_password, user_exist.password)
        if not verfy_pass:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid password")
        
        query.update({"password": user.password}, synchronize_session=False)
        db.commit()
        return {"data": "success"}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User doesn't exist")
    

# ***************UPLOAD USER IMAGE*******************
@router.post("/user/upload/")
def upload_user_image(file: UploadFile ):

    # Define the directory to save uploaded images
    UPLOAD_DIRECTORY = "uploads/users/"

    # Create the upload directory if it doesn't exist
    os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)

    # Generate a unique filename for the uploaded image
    file_extension = file.filename.split(".")[-1]
    filename = f"{str(uuid.uuid4())}.{file_extension}"
    
    try:
        # Save the uploaded file to the specified directory
        with open(os.path.join(UPLOAD_DIRECTORY+filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {"filename" : filename}
    
    except Exception as e:
        return JSONResponse(content={"message": f"Failed to upload file: {str(e)}"}, status_code=500)
 

# ***************UPDATE IMAGE*******************
@router.post("/user/image", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def update_personal_image(img: schemas.PersonalImg, db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    query = db.query(models.User).filter(models.User.id == current_user.id)
    
    #details exist
    details_exist = query.first()
    if details_exist:
        query.update(img.model_dump(), synchronize_session=False)
        db.commit()
        return query.first()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")



# ***************GET USER DETAILS*******************
@router.get("/user", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_personal_details(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
    results =  db.query(models.User).filter(current_user.id == models.User.id).first()
    if not results:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No personal details found.")
    
    return results


#get all users
# @router.get("/users", status_code=status.HTTP_200_OK, response_model=List[schemas.UserResponse])
# def get_users(db: Session = Depends(get_db), current_user: str = Depends(oauth2.get_current_user)):
#     uza =  db.query(models.User).all()
#     return uza