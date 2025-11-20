from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/trilhas", tags=["Trilhas"])


@router.get("/{usuario_id}", response_model=List[schemas.TrilhaResponse])
def listar_trilha_usuario(usuario_id: int, db: Session = Depends(get_db)):
    trilhas = (
        db.query(models.Trilha)
        .filter(models.Trilha.id_usuario == usuario_id)
        .all()
    )
    return trilhas
