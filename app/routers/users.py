from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import bcrypt

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.get("/", response_model=List[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(models.Usuario).all()
    return usuarios


@router.post("/registrar", response_model=schemas.UsuarioResponse, status_code=status.HTTP_201_CREATED)
def registrar_usuario(dados: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica se o e-mail já está cadastrado
    usuario_existente = (
        db.query(models.Usuario)
        .filter(models.Usuario.email == dados.email)
        .first()
    )

    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já cadastrado"
        )

    # Gera hash seguro da senha
    senha_hash = bcrypt.hashpw(dados.senha.encode(), bcrypt.gensalt()).decode()

    novo_usuario = models.Usuario(
        nome=dados.nome,
        email=dados.email,
        senha_hash=senha_hash,
        nivel=dados.nivel,
        cargo=dados.cargo
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario
