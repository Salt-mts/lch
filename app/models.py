from .database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    sex = Column(String, nullable=True)
    image = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    verification_code = Column(Integer, default=111111, nullable=False)
    email_verified = Column(Integer, default=0, nullable=False)
    date_created = Column(TIMESTAMP(timezone=False), server_default=text("now()"), nullable=False)




class Business(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    about = Column(Text, nullable=True)
    category = Column(String, nullable=True)
    work_experience = Column(Text, nullable=True)
    years_of_experience = Column(Integer, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    days = Column(String, nullable=True)
    hour_from = Column(String, nullable=True)
    hour_to = Column(String, nullable=True)
    website = Column(String, nullable=True)
    facebook = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    twitter = Column(String, nullable=True)
    linkedin = Column(String, nullable=True)

    owner = relationship("User")


class Comments(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    msg = Column(Text, nullable=False)
    business_id = Column(Integer, ForeignKey("business.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(Integer, nullable=False)
    parentuser_id = Column(Integer, nullable=True)
    date_created = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    parentcat_id = Column(Integer, nullable=False)