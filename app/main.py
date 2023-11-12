from fastapi import FastAPI
from .routes import users, auth, business, category, catalog, certifications
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ************************ CORS ************************
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(business.router)
app.include_router(catalog.router)
app.include_router(certifications.router)
app.include_router(category.router)
