from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/login", response_model=schemas.LoginResponse)
def login(dados: schemas.LoginRequest, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == dados.email).first()

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    # Aqui estamos só comparando texto puro porque no banco tem mock.
    # No projeto de segurança você mostra o hash de verdade.
    if usuario.senha_hash != dados.senha:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    return schemas.LoginResponse(
        message="Login realizado com sucesso",
        usuario_id=usuario.id_usuario
    )
