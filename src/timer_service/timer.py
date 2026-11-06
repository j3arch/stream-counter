import datetime as dt
import asyncio
import config
import json
import os
from pathlib import Path

class Timer:
    def __init__(self, initial_seconds: int) -> None:
        self.remaining_seconds = initial_seconds
        self.paused = False
        self.cap_seconds = config.TIMER_CAP_SECONDS                 # Add to the notes!
        self.has_hit_cap = False
        self.base_dir = Path(__file__).resolve().parent
        self.state_file = self.base_dir / "timer_state.json"
        self.milestone_file = self.base_dir / "milestones.txt"

        # Milestone tracker (for subs/donations)
        self.sub_progress = 0
        self.gifts_owed = 0
        self.donation_progress = 0

    def add_subs_to_milestone(self, amount: int) -> None:
        self.sub_progress += amount

        while self.sub_progress >= 20:
            self.sub_progress -= 20
            self.gifts_owed += 1
            print(f"Milestone reached! Gifts owed {self.gifts_owed}")

    def add_donations_to_milestone(self, amount: float) -> None: 
        self.donation_progress += amount

        while self.donation_progress >= 50.0:
            self.donation_progress -= 50.0
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

    # implement save state
    
    def save_state(self) -> None:
        state = {
            "remaining_seconds": self.remaining_seconds,
            "paused": self.paused,
            "sub_progress": self.sub_progress,
            "donation_progress": self.donation_progress,
            "gifts_owed": self.gifts_owed,
            "has_hit_cap": self.has_hit_cap
        }
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(state, f)

    def load_state(self) -> None:
        if not os.path.exists(self.state_file):
            return

        with open(self.state_file, "r", encoding="utf-8") as f:
            state = json.load(f)

        self.remaining_seconds = state.get("remaining_seconds", self.remaining_seconds)
        self.paused = state.get("paused", self.paused)
        self.sub_progress = state.get("sub_progress", self.sub_progress)
        self.donation_progress = state.get("donation_progress", self.donation_progress)
        self.gifts_owed = state.get("gifts_owed", self.gifts_owed)
        self.has_hit_cap = state.get("has_hit_cap", self.has_hit_cap)

    def tick(self) -> None:
        if self.remaining_seconds > 0 and not self.paused:
            self.remaining_seconds -= 1

    def is_finished(self) -> bool:
        return self.remaining_seconds <= 0

    def add_seconds(self, amount: int) -> None:
        if self.has_hit_cap:
            print("Cap has been reached, no more time can be added")   # Add to the notes!
            return
        
        new_total = max(0, self.remaining_seconds + amount)                 

        if new_total >= self.cap_seconds:
            self.remaining_seconds = self.cap_seconds                     
            self.has_hit_cap = True
            print("Cap has been reached, no more time can be added")
        else:
            self.remaining_seconds = new_total


    def format(self) -> str:
        return str(dt.timedelta(seconds=self.remaining_seconds))

    def reset_state(self) -> None:
        self.remaining_seconds = 0
        self.paused = False
        self.sub_progress = 0
        self.donation_progress = 0
        self.gifts_owed = 0
        self.has_hit_cap = False
        self.save_state()


async def run_timer(timer: Timer) -> None:
    while not timer.is_finished():
        with open("timer.txt", "w", encoding="utf-8") as f:
            f.write(timer.format())

        with open("milestones.txt", "w", encoding="utf-8") as f:
            f.write(f"Gifts owed: {timer.gifts_owed}")
        
        await asyncio.sleep(1)
        timer.tick()
        timer.save_state()
    
    print("Stream ended!")