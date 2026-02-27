import socketio
import config
from timer_service import Timer

sio = socketio.AsyncClient()

def setup_socker(timer: Timer) -> None:
    pass