from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/sensores", tags=["Sensores"])


@router.get("/", response_model=List[schemas.SensorResponse])
def listar_sensores(db: Session = Depends(get_db)):
    return db.query(models.SensorData).all()
