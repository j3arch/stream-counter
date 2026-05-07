import asyncio
from timer_service import Timer

async def terminal_controller(timer: Timer) -> None:
    print("Terminal controls active.")
    print("Use: pause/resume/claim, or a number like 60 / -30")

    while True:
        raw = await asyncio.to_thread(input, "> ")
        cmd = raw.strip().lower()

        if cmd == "pause":
            timer.pause()
            print("Timer paused")
            continue

        if cmd == "resume":
            timer.resume()
            print("Timer resumed")
            continue

        if cmd == "claim":
            timer.claim_gift()
            print("Gift claimed")
            continue


        try:
            amount = int(raw)
        except ValueError:
            print("Invalid input. Use pause, resume, or a whole number.")
            continue

        timer.add_seconds(amount)
        print(f"Adjusted timer by {amount}s. Current: {timer.format()}")