from .database import Base
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    verifcation_code = Column(Integer, default=111111, nullable=False)
    email_verified = Column(Integer, default=0, nullable=False)
    date_created = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)


class Personal(Base):
    __tablename__ = "personal"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    sex = Column(String, nullable=True)
    modified_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)

class Addresses(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    country = Column(String, nullable=False)


class Business(Base):
    __tablename__ = "business"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    about = Column(String, nullable=True)
    hour_from = Column(String, nullable=True)
    hour_to = Column(String, nullable=True)
    days = Column(String, nullable=True)
    website = Column(String, nullable=True)
    facebook = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    twitter = Column(String, nullable=True)


class PersonalImg(Base):
    __tablename__ = "profile_img"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    image = Column(String, nullable=False, default="user.png")
    modified_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"), nullable=False)