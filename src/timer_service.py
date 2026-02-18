import time
import datetime as dt

class Timer:
    def __init__(self, initial_seconds: int) -> None:
        self.remaining_seconds = initial_seconds

    def tick(self) -> None:
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1

    def is_finished(self) -> bool:
        return self.remaining_seconds <= 0

    def add_seconds(self, amount: int) -> None:
        self.remaining_seconds += amount

    def format(self) -> str:
        return str(dt.timedelta(seconds=self.remaining_seconds))

def countdown(initial_seconds: int):
    timer = Timer(initial_seconds)
    while not timer.is_finished():
        with open("timer.txt", "w", encoding="utf-8") as f:
            f.write(timer.format())
        time.sleep(1)
        timer.tick()
    print("Stream ended!")

user_input = input("Enter the time in seconds: ")

countdown(int(user_input))