from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- Schemas para Criação (Input) ---

class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str

class CursoCreate(BaseModel):
    nome: str
    codigo: str
    descricao: str

class MatriculaCreate(BaseModel):
    aluno_id: int
    curso_id: int

# --- Schemas para Resposta (Output) ---

class Aluno(BaseModel):
    id: int
    nome: str
    email: EmailStr
    telefone: str

    class Config:
        from_attributes = True

class Curso(BaseModel):
    id: int
    nome: str
    codigo: str
    descricao: str

    class Config:
        from_attributes = True

class Matricula(BaseModel):
    id: int
    aluno_id: int
    curso_id: int

    class Config:
        from_attributes = True

Cursos = List[Curso]