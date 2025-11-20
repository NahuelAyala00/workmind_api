from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    nivel: Optional[str] = None
    cargo: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    id_usuario: int
    data_criacao: Optional[datetime] = None

    class Config:
        orm_mode = True


class CursoBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    categoria: Optional[str] = None
    carga_horaria: Optional[int] = None
    nivel_recomendado: Optional[str] = None


class CursoResponse(CursoBase):
    id_curso: int

    class Config:
        orm_mode = True


class TrilhaResponse(BaseModel):
    id_trilha: int
    id_usuario: int
    id_curso: int
    progresso: int
    status: str

    class Config:
        orm_mode = True


class SensorResponse(BaseModel):
    id_sensor: int
    temperatura: float
    luminosidade: int
    ruido: int
    origem: str

    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


class LoginResponse(BaseModel):
    message: str
    usuario_id: int
