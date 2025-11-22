from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_trilha_usuario_1():
    """
    CT07 - Listar trilha do usuário 1
    """
    response = client.get("/trilhas/1")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    # se quiser forçar que exista pelo menos uma trilha:
    # assert len(data) >= 1
