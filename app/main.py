from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import crud, schemas,models
from .database import engine, get_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Wildlife Conservation API"}


@app.post("/animals/", response_model=schemas.Animal)
def create_animal_view(data: schemas.AnimalCreate, db: Session = Depends(get_db)):
    return crud.create_animal(db=db, animal=data)

@app.get("/animals/{animal_id}", response_model=schemas.Animal)
def read_animal_view(animal_id: int, db: Session = Depends(get_db)):
    return crud.get_animal(db=db, animal_id=animal_id)

@app.put("/animals/{animal_id}", response_model=schemas.Animal)
def update_animal_view(animal_id: int, data: schemas.AnimalUpdate, db: Session = Depends(get_db)):
    return crud.update_animal(db=db, animal_id=animal_id, animal=data)

@app.delete("/animals/{animal_id}")
def delete_animal_view(animal_id: int, db: Session = Depends(get_db)):
    return crud.delete_animal(db=db, animal_id=animal_id)

@app.post("/guiders/", response_model=schemas.Guider)
def create_guider_view(data: schemas.GuiderCreate, db: Session = Depends(get_db)):
    return crud.create_guider(db=db, guider=data)

@app.get("/guiders/{guider_id}", response_model=schemas.Guider)
def read_guider_view(guider_id: int, db: Session = Depends(get_db)):
    return crud.get_guider(db=db, guider_id=guider_id)

@app.put("/guiders/{guider_id}", response_model=schemas.Guider)
def update_guider_view(guider_id: int, data: schemas.GuiderUpdate, db: Session = Depends(get_db)):
    return crud.update_guider(db=db, guider_id=guider_id, guider=data)

@app.delete("/guiders/{guider_id}")
def delete_guider_view(guider_id: int, db: Session = Depends(get_db)):
    return crud.delete_guider(db=db, guider_id=guider_id)


@app.post("/guests/", response_model=schemas.Guest)
def create_guest_view(data: schemas.GuestCreate, db: Session = Depends(get_db)):
    return crud.create_guest(db=db, guest=data)

@app.get("/guests/{guest_id}", response_model=schemas.Guest)
def read_guest_view(guest_id: int, db: Session = Depends(get_db)):
    return crud.get_guest(db=db, guest_id=guest_id)

@app.put("/guests/{guest_id}", response_model=schemas.Guest)
def update_guest_view(guest_id: int, data: schemas.GuestUpdate, db: Session = Depends(get_db)):
    return crud.update_guest(db=db, guest_id=guest_id, guest=data)

@app.delete("/guests/{guest_id}")
def delete_guest_view(guest_id: int, db: Session = Depends(get_db)):
    return crud.delete_guest(db=db, guest_id=guest_id)


@app.get("/animals/", response_model=List[schemas.Animal])
def list_animals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_animals(db=db, skip=skip, limit=limit)

@app.get("/guiders/", response_model=List[schemas.Guider])
def list_guiders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_guiders(db=db, skip=skip, limit=limit)

@app.get("/guests/", response_model=List[schemas.Guest])
def list_guests(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_guests(db=db, skip=skip, limit=limit)