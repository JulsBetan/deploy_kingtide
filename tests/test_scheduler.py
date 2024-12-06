import pytest
import responses
from update_events_scheduler import update_events, UPDATE_EVENTS_URL

@responses.activate
def test_update_events_successful():
    """Prueba que verifica si la función maneja correctamente una respuesta exitosa."""
    responses.add(
        responses.POST,
        UPDATE_EVENTS_URL,
        json={"message": "Eventos actualizados exitosamente"},
        status=200
    )

    update_events()
    assert len(responses.calls) == 1
    assert responses.calls[0].response.status_code == 200

@responses.activate
def test_update_events_server_error():
    """Prueba que verifica cómo la función maneja un error 500 del servidor."""
    responses.add(
        responses.POST,
        UPDATE_EVENTS_URL,
        status=500
    )

    update_events()
    assert len(responses.calls) == 1
    assert responses.calls[0].response.status_code == 500

@responses.activate
def test_update_events_exception_handling():
    """Prueba que verifica cómo se maneja una excepción durante la solicitud."""
    responses.add(
        responses.POST,
        UPDATE_EVENTS_URL,
        body=Exception("Conexión fallida")
    )

    update_events()
    assert len(responses.calls) == 1
