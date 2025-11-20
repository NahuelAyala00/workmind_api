from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/cursos", tags=["Cursos"])


@router.get("/", response_model=List[schemas.CursoResponse])
def listar_cursos(db: Session = Depends(get_db)):
    return db.query(models.Curso).all()


@router.post("/", response_model=schemas.CursoResponse)
def criar_curso(curso: schemas.CursoBase, db: Session = Depends(get_db)):
    novo = models.Curso(**curso.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
