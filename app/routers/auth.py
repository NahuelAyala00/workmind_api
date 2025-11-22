from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import bcrypt

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/login", response_model=schemas.LoginResponse)
def login(dados: schemas.LoginRequest, db: Session = Depends(get_db)):
    usuario = (
        db.query(models.Usuario)
        .filter(models.Usuario.email == dados.email)
        .first()
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    # Verificando senha com bcrypt
    senha_digitada = dados.senha.encode()
    senha_hash_salva = usuario.senha_hash.encode()

    if not bcrypt.checkpw(senha_digitada, senha_hash_salva):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    return schemas.LoginResponse(
        message="Login realizado com sucesso",
        usuario_id=usuario.id_usuario
    )
