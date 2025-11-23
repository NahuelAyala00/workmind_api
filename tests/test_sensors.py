from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_listar_sensores():
    """
    CT08 - Listar sensores deve retornar dados de IoT
    """
    response = client.get("/sensores/")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    if data:
        primeiro = data[0]
        assert "temperatura" in primeiro
        assert "luminosidade" in primeiro
        assert "ruido" in primeiro
