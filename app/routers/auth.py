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

    senha_digitada = dados.senha.encode("utf-8")
    senha_salva = usuario.senha_hash or ""

    # Verifica se a senha salva "parece" hash bcrypt
    is_bcrypt = (
        senha_salva.startswith("$2a$")
        or senha_salva.startswith("$2b$")
        or senha_salva.startswith("$2y$")
    )

    senha_ok = False

    if is_bcrypt:
        # Tentando validar hash bcrypt corretamente
        try:
            senha_ok = bcrypt.checkpw(
                senha_digitada,
                senha_salva.encode("utf-8")
            )
        except ValueError:
            # Hash inválido → considera senha incorreta
            senha_ok = False
    else:
        # Senha mock em texto puro (para testes)
        senha_ok = (dados.senha == senha_salva)

    if not senha_ok:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    return schemas.LoginResponse(
        message="Login realizado com sucesso",
        usuario_id=usuario.id_usuario
    )
