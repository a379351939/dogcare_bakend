from fastapi import FastAPI
from datetime import date
from app.db.session import SessionLocal
from app.models.dog import Dog

app = FastAPI()

@app.post("/create_dog")
def create_dog(name:str, birthday: date):
    db = SessionLocal()
    dog = Dog(name=name, birthday=birthday)
    db.add(dog)
    db.commit()
    return {"id":dog.id,"name": dog.name}