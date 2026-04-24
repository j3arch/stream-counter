import asyncio
from timer_service import Timer

async def terminal_controller(timer: Timer) -> None:
    print("Terminal controls active.")
    print("Use: pause/resume, or a number like 60 / -30")

    while True:
        raw_input = await asyncio.to_thread(input, "> ")
        cmd = raw_input.strip().lower()

        if cmd == "pause":
            timer.paused = True
        elif cmd == "resume":
            timer.paused = False
        else:
            try:
                amount = int(raw_input)
            except ValueError:
                print("Invalid input. Use pause, resume, or a whole number.")
                continue

            timer.add_seconds(amount)
            print(f"Adjusted timer by {amount}s. Current: {timer.format()}")