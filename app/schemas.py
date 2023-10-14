from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ***********USER SCHEMAS*************
class RegisterUser(BaseModel):
    email: EmailStr
    password: str


class Password(BaseModel):
    password: str

class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    sex: Optional[str]
    image: Optional[str]
    is_active: bool
    date_created: datetime
    verification_code: Optional[int]
    email_verified: Optional[int]

class UserOut(BaseModel):
    id: int
    email: EmailStr
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    sex: Optional[str]
    image: Optional[str]
    is_active: bool
    date_created: datetime
    email_verified: Optional[int]
    

class Personal(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    phone: Optional[str]
    sex: Optional[str]

class PersonalImg(BaseModel):
    user_id: int
    image: str

# authentication
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


#************ RESPOSNSE MODELS ******************
class RegResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    date_created: datetime

    class Config:
        from_attributes = True


class UserResponse(RegResponse):
    pass
    # firstname: Optional[str]
    # lastname: Optional[str]
    # phone: Optional[int]
    # address: Optional[str]
    # city: Optional[str]
    # state: Optional[str]
    # country: Optional[str]

    class Config:
        from_attributes = True


#************ BUSINESS MODELS ******************
class Business(BaseModel):
    id: int
    name: str
    about: Optional[str]
    category: Optional[str]
    years_of_experience: Optional[int]
    work_experience: Optional[str]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    days: Optional[str]
    hour_from: Optional[str]
    hour_to: Optional[str]
    website: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    twitter: Optional[str]
    linkedin: Optional[str]
    owner: UserOut


class BusinessAbout(BaseModel):
    name: str
    about: Optional[str]
    category: Optional[str]

class BusinessExperience(BaseModel):
    work_experience: Optional[str]
    years_of_experience: Optional[int]

class BusinessAddress(BaseModel):
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]

class BusinessSocial(BaseModel):
    website: Optional[str]
    facebook: Optional[str]
    instagram: Optional[str]
    twitter: Optional[str]
    linkedin: Optional[str]

class BusinessHour(BaseModel):
    days: Optional[str]
    hour_from: Optional[str]
    hour_to: Optional[str]