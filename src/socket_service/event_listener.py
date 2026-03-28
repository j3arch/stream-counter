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


        if event_type in ("subscription", "resub", "subgift", "gifted"):
            for msg in messages:
                count = int(msg.get("amount", 1))
                base_added = count * config.SECONDS_PER_SUB
                timer.add_seconds(base_added)

                # add sub bonuses

        if event_type == 'bits':
            for msg in messages:
                bits = int(msg.get('amount', 0))
                added = (bits // 100) * config.SECONDS_PER_100_BITS
                timer.add_seconds(added)


        if event_type == "donation":
            for msg in messages:
                donation = float(msg.get("amount", 0))
                added = int(donation * config.SECONDS_PER_1_USD)
                timer.add_seconds(added)

                # add donation bonuses



async def streamlabs_event_listener(timer: Timer) -> None: 
    setup_socket(timer)  #connects to the websocket and waits for the events

    url = f"https://sockets.streamlabs.com?token={config.STREAMLABS_SOCKET_TOKEN}"

    await sio.connect(url)
    await sio.wait()