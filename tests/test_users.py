from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_usuarios_status_code():
    """
    CT03 - Listar usuários deve retornar 200 OK
    """
    response = client.get("/usuarios/")
    assert response.status_code == 200


def test_listar_usuarios_contem_nahuel():
    """
    CT04 - Lista de usuários deve conter o usuário Nahuel (mock inserido no banco)
    """
    response = client.get("/usuarios/")
    assert response.status_code == 200

    data = response.json()
    nomes = [u["nome"] for u in data]

    assert "Nahuel Ayala" in nomes
