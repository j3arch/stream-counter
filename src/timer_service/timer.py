import datetime as dt
import asyncio
# import json
# import os

class Timer:
    def __init__(self, initial_seconds: int) -> None:
        # self.state_file = "timer_state.json"
        self.remaining_seconds = initial_seconds

    # def _load_state(self, default: int) -> int:
        # return 0

    def tick(self) -> None:
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1

    def is_finished(self) -> bool:
        return self.remaining_seconds <= 0

    def add_seconds(self, amount: int) -> None:
        self.remaining_seconds += amount

    def format(self) -> str:
        return str(dt.timedelta(seconds=self.remaining_seconds))

async def run_timer(timer: Timer) -> None:
    while not timer.is_finished():
        with open("timer.txt", "w", encoding="utf-8") as f:
            f.write(timer.format())
        
        await asyncio.sleep(1)
        timer.tick()
    
    print("Stream ended!")