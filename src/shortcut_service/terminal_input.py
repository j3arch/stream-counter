import asyncio
from timer_service import Timer

async def terminal_controller(timer: Timer) -> None:
    print("Terminal controls active.")
    print("Use: pause/resume, or a number like 60 / -30")

    while True:
        raw = await asyncio.to_thread(input, "> ")
        cmd = raw.strip().lower()

        if cmd == "pause":
            timer.paused = True
        elif cmd == "resume":
            timer.paused = False
        