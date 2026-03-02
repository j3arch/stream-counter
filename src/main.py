# import os
# from dotenv import load_dotenv
# from twitchio.ext import commands
import asyncio
from timer_service import Timer, run_timer
from socket_service.event_listener import streamlabs_event_listener

async def main() -> None:
    initial_time = 7200
    shared_timer = Timer(initial_time)
    print("Stream starting...")

    await asyncio.gather(
        run_timer(shared_timer),
        streamlabs_event_listener(shared_timer)
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStream ended!")