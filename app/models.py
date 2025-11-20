from sqlalchemy import Column, Integer, String, Text, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False, unique=True, index=True)
    senha_hash = Column(String(255), nullable=False)
    nivel = Column(String(50))
    cargo = Column(String(100))
    data_criacao = Column(TIMESTAMP)

    trilhas = relationship("Trilha", back_populates="usuario")


class Curso(Base):
    __tablename__ = "curso"

    id_curso = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text)
    categoria = Column(String(100))
    carga_horaria = Column(Integer)
    nivel_recomendado = Column(String(50))

    trilhas = relationship("Trilha", back_populates="curso")


class Trilha(Base):
    __tablename__ = "trilha"

    id_trilha = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_curso = Column(Integer, ForeignKey("curso.id_curso"), nullable=False)
    progresso = Column(Integer)
    status = Column(String(20))
    data_inicio = Column(TIMESTAMP)
    data_conclusao = Column(TIMESTAMP)

    usuario = relationship("Usuario", back_populates="trilhas")
    curso = relationship("Curso", back_populates="trilhas")


class SensorData(Base):
    __tablename__ = "sensordata"

    id_sensor = Column(Integer, primary_key=True, index=True)
    temperatura = Column(Numeric(5, 2))
    luminosidade = Column(Integer)
    ruido = Column(Integer)
    origem = Column(String(50))
    data_hora = Column(TIMESTAMP)
