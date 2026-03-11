import socketio
import config
from timer_service import Timer

sio = socketio.AsyncClient() # socket.io client

def setup_socket(timer: Timer) -> None:
    @sio.on('connect')
    async def on_connect() -> None:
        print("Connected to Streamlabs API!")

    @sio.on('event')
    async def on_event(data: dict) -> None:
        event_type = data.get('type')
        messages = data.get('message', [])


        if event_type == 'subscription' or event_type == 'resub':
            timer.add_seconds(config.SECONDS_PER_SUB)

        if event_type == 'bits':
            timer.add_seconds(config.SECONDS_PER_100_BITS) # placeholder, adjust price per bit

    # setup the api calls to get the sub/bits/dono calls, calculate the amount of time that needs to be added + add it to the timer.
    # optionally add a message of how much was added


async def streamlabs_event_listener(timer: Timer) -> None: 
    setup_socket(timer)  #connects to the websocket and waits for the events

    url = f"https://sockets.streamlabs.com?token={config.STREAMLABS_SOCKET_TOKEN}"

    await sio.connect(url)
    await sio.wait()