"""
Este módulo contiene un servicio programado para actualizar eventos
mediante una llamada periódica al endpoint de actualización de eventos.

- Llama a un endpoint para actualizar eventos cada 2 horas.
- Registra el estado de las actualizaciones en los logs.
"""

import time
from datetime import datetime
import logging
import requests
import schedule

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

UPDATE_EVENTS_URL = "http://api_deportes:8000/api/events/update-events"


def update_events():
    """
    Función para programar el llamado al end-point de uptate events para mantener actualizada
    la tabla de próximos eventos.
    """
    try:
        response = requests.post(UPDATE_EVENTS_URL, timeout=(5, 120))
        if response.status_code == 200:
            update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info("Actualización exitosa a las: %s", update_time)
        else:
            logging.error("Error al actualizar: %s, %s", response.status_code, response.text)
    except requests.exceptions.Timeout:
        logging.error("La solicitud al endpoint superó el tiempo de espera.")
    except requests.exceptions.RequestException as e:
        logging.error("Error al llamar al endpoint: %s", e)


if __name__ == "__main__":
    schedule.every(2).hours.do(update_events)

    logging.info("Servicio programado para actualizar eventos cada 2 horas.")
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Servicio detenido manualmente.")
