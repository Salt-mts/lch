from fastapi import FastAPI
from .routes import users, auth, business, category, catalog, certifications, comments, messages, rating, subscriptions, reset_password
from .admin_routes import admin_auth, admin_users, admin_business, admin_subscription, admin_details
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
# from .database import engine
# from . import models
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

# models.Base.metadata.create_all(bind=engine)

# make uploads folder readable from outside world
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

#start scheduler
# jobs.scheduler.start()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(reset_password.router)
app.include_router(business.router)
app.include_router(messages.router)
app.include_router(catalog.router)
app.include_router(certifications.router)
app.include_router(comments.router)
app.include_router(rating.router)
app.include_router(subscriptions.router)
app.include_router(category.router)

# admin routes
app.include_router(admin_auth.router)
app.include_router(admin_details.router)
app.include_router(admin_users.router)
app.include_router(admin_business.router)
app.include_router(admin_subscription.router)
