from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login_sucesso():
    """
    CT01 - Login com credenciais válidas
    """
    payload = {
        "email": "nahuel@example.com",
        "senha": "hash_senha_teste"  # igual ao que está no banco
    }

    response = client.post("/auth/login", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Login realizado com sucesso"
    assert data["usuario_id"] == 1


def test_login_senha_incorreta():
    """
    CT02 - Login com senha incorreta
    """
    payload = {
        "email": "nahuel@example.com",
        "senha": "senha_errada"
    }

    response = client.post("/auth/login", json=payload)

    assert response.status_code == 401
    data = response.json()
    assert "Credenciais inválidas" in data["detail"]
