import datetime as dt
import asyncio
# import json
# import os

class Timer:
    def __init__(self, initial_seconds: int) -> None:
        # self.state_file = "timer_state.json"
        self.remaining_seconds = initial_seconds
        self.paused = False

        # Milestone tracker (for subs)
        self.sub_progress = 0
        self.gifts_owed = 0

    def add_subs_to_milestone(self, amount: int) -> None:
        self.sub_progress += amount

        while self.sub_progress >= 20:
            self.sub_progress -= 20
            self.gifts_owed += 1
            print(f"Milestone reached! Gifts owed {self.gifts_owed}")

    def claim_gift(self) -> None:
        if self.gifts_owed > 0:
            self.gifts_owed -= 1
            print(f"Gift claimed! Remaining: {self.gifts_owed}")
        else:
            print("No gifts owed")

    def pause(self) -> None:
        self.paused = True
    
    def resume(self) -> None:
        self.paused = False

    # implement safe state
    """
    def _load_state(self, default: int) -> int:
        return default

    def _save_state(self) -> None:
        with open(self.state_file, "w") as f:
            json.dump({"remaining_seconds": self.remaining_seconds}, f)
    """ 

    def tick(self) -> None:
        if self.remaining_seconds > 0 and not self.paused:
            self.remaining_seconds -= 1

    def is_finished(self) -> bool:
        return self.remaining_seconds <= 0

    def add_seconds(self, amount: int) -> None:
        self.remaining_seconds = max(0, self.remaining_seconds + amount)

    def format(self) -> str:
        return str(dt.timedelta(seconds=self.remaining_seconds))

async def run_timer(timer: Timer) -> None:
    while not timer.is_finished():
        with open("timer.txt", "w", encoding="utf-8") as f:
            f.write(timer.format())

        with open("milestones.txt", "w", encoding="utf-8") as f:
            f.write(f"Gifts owed: {timer.gifts_owed}")
        
        await asyncio.sleep(1)
        timer.tick()
    
    print("Stream ended!")