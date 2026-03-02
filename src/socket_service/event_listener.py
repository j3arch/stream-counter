import socketio
import config
from timer_service import Timer

sio = socketio.AsyncClient() # socket.io client

def setup_socker(timer: Timer) -> None:
    pass


async def streamlabs_event_listener(timer: Timer) -> None: 
    setup_socker(timer)  #connects to the websocket and waits for the events

    url = f"https://sockets.streamlabs.com?token={config.STREAMLABS_SOCKET_TOKEN}"

    await sio.connect(url)
    await sio.wait()