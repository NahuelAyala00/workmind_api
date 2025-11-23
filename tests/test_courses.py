from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_cursos():
    """
    CT05 - Listar cursos deve retornar 200 e uma lista
    """
    response = client.get("/cursos/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1  # pelo menos 1 curso mockado


def test_criar_curso():
    """
    CT06 - Criar curso via POST /cursos/
    """
    novo_curso = {
        "titulo": "Curso de Testes Automatizados",
        "descricao": "Introducao a testes com pytest.",
        "categoria": "Testes",
        "carga_horaria": 8,
        "nivel_recomendado": "junior"
    }

    response = client.post("/cursos/", json=novo_curso)
    assert response.status_code == 200

    data = response.json()
    assert data["titulo"] == novo_curso["titulo"]
    assert data["categoria"] == "Testes"
