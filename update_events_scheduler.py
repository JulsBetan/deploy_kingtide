import time
import requests
from datetime import datetime

# UPDATE_EVENTS_URL = "http://localhost:8000/events/update-events"
UPDATE_EVENTS_URL = "http://api_deportes:8000/events/update-events"

def update_events():
    try:
        response = requests.post(UPDATE_EVENTS_URL)
        if response.status_code == 200:
            update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Actualización exitosa a las: {update_time}")
        else:
            print(f"Error al actualizar: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error al llamar al endpoint: {e}")

if __name__ == "__main__":
    import schedule
    schedule.every(10).minutes.do(update_events)

    print("Servicio programado para actualizar eventos cada 2 horas.")
    while True:
        schedule.run_pending()
        time.sleep(1)
