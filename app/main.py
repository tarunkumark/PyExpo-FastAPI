from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Create a route function to create a user using POST method
        



#Create a route function to get all users using GET method
        



#Create a route to get a user by id using GET method




#Create a route function to create an item for a user using POST method
        



#Create a route function to get all items using GET method
        



#Create a route function to get all items by title using GET method
        



#Create a route function to get all items by owner using GET method
        



    




