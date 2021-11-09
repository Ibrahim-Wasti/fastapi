from fastapi import FastAPI
from . import models
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#from .database import engine
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Allow cross origin access to the api
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], #what methods are allowed to be accessed
    allow_headers=["*"], #what headers are allowed to be accessed
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message":"Welcome home"}

