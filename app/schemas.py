from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# user
class RegisterUser(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: int
    email: EmailStr
    password: str
    is_active: bool
    date_created: datetime
    verification_code: Optional[int]
    email_verified: Optional[int]

class Personal(BaseModel):
    firstname: str
    lastname: str
    phone: str
    sex: Optional[str]

class Addresses(BaseModel):
    id: int
    user_id: int
    address: str
    city: str
    state: str
    country: str

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


class PersonalResponse(Personal):
    user_id: int

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


