# import os
# from dotenv import load_dotenv
# from twitchio.ext import commands
import asyncio
from timer_service import Timer, run_timer

async def main() -> None:
    initial_time = 7200
    shared_timer = Timer(initial_time)
    print("Stream starting...")

    await asyncio.gather(
        run_timer(shared_timer),
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStream ended!")