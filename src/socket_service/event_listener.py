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
        # This will show you exactly what Twitch/Streamlabs is calling the event
        # print(f"DEBUG: Received event of type '{data.get('type')}'")
        # print(f"DEBUG: Full data: {data}")

        event_type = data.get('type')
        messages = data.get('message', [])


        if event_type == 'bits':
            for msg in messages:
                bits = int(msg.get('amount', 0))
                added = (bits // 100) * config.SECONDS_PER_100_BITS
                timer.add_seconds(added)
                print(f"Processed {bits} bits. Added {added}s") # TEST


        if event_type in ("subscription", "resub", "subMysteryGift"):
            total_subs_in_event = 0
            for msg in messages:
                count = int(msg.get("amount", 1))
                total_subs_in_event += count

            base_added = total_subs_in_event * config.SECONDS_PER_SUB
            timer.add_seconds(base_added)
            print(f"Processed {total_subs_in_event}subs. Added {base_added}s") # TEST

            if total_subs_in_event >= 20:
                timer.add_seconds(config.BONUS_SECONDS_PER_20_SUBS)
            elif total_subs_in_event >= 10:
                timer.add_seconds(config.BONUS_SECONDS_PER_10_SUBS)
            elif total_subs_in_event >= 5:
                timer.add_seconds(config.BONUS_SECONDS_PER_5_SUBS)

            


        if event_type == "donation":
            for msg in messages:
                donation = float(msg.get("amount", 0))
                added = int(donation * config.SECONDS_PER_1_USD)
                timer.add_seconds(added)
                print(f"Processed {donation}$. Added {added}s") # TEST

                if donation >= 100:
                    timer.add_seconds(config.BONUS_SECONDS_PER_100_USD)
                    print("Processed 100.0$ bonus! Added 600s")
                elif donation >= 25:
                    timer.add_seconds(config.BONUS_SECONDS_PER_25_USD)
                    print("Processed 25.0$ bonus! Added 150s")
                
                



async def streamlabs_event_listener(timer: Timer) -> None: 
    setup_socket(timer)  #connects to the websocket and waits for the events

    url = f"https://sockets.streamlabs.com?token={config.STREAMLABS_SOCKET_TOKEN}"

    await sio.connect(url)
    await sio.wait()