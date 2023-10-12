import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/lchapp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# try:
#     conn = psycopg2.connect(database="db_name", host="localhost", user="postgres", password="postgres")
#     cur = conn.cursor()
#     print(conn)
# except Exception as error:
#     print("connection failed")
#     print("error", error)

