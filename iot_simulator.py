import random
import time
import datetime

from app.database import SessionLocal
from app import models


def gerar_leitura(origem: str = "home-office") -> models.SensorData:
    """
    Gera uma leitura simulada de sensores IoT
    """
    temperatura = round(random.uniform(22.0, 32.0), 2)   # 22°C a 32°C
    luminosidade = random.randint(150, 700)              # 150 a 700 lux
    ruido = random.randint(30, 85)                       # 30 a 85 dB

    leitura = models.SensorData(
        temperatura=temperatura,
        luminosidade=luminosidade,
        ruido=ruido,
        origem=origem,
        data_hora=datetime.datetime.now()
    )

    return leitura


def main(qtd_registros: int = 10, intervalo_segundos: float = 1.0):
    """
    Insere leituras simuladas na tabela sensordata.
    qtd_registros: quantas leituras serão geradas
    intervalo_segundos: tempo entre uma leitura e outra
    """
    db = SessionLocal()
    try:
        for i in range(qtd_registros):
            leitura = gerar_leitura("home-office")

            db.add(leitura)
            db.commit()
            db.refresh(leitura)

            print(
                f"[{i+1}/{qtd_registros}] "
                f"Inserido sensor ID={leitura.id_sensor} | "
                f"T={leitura.temperatura}°C | "
                f"L={leitura.luminosidade} lux | "
                f"R={leitura.ruido} dB | "
                f"origem={leitura.origem}"
            )

            time.sleep(intervalo_segundos)
    finally:
        db.close()


if __name__ == "__main__":
    # Gera 10 leituras, 1 por segundo
    main(qtd_registros=10, intervalo_segundos=1.0)
