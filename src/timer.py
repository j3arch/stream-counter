import time
import datetime as dt

class Timer:
    def __init__(self, initial_seconds: int):
        self.remaining_seconds = initial_seconds

    def tick(self) -> None:
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1

    def is_finished(self):
        return self.remaining_seconds <= 0

    def add_seconds(self, amount: int):
        self.remaining_seconds += amount

    def format(self):
        return str(dt.timedelta(seconds=self.remaining_seconds))

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        with open("timer.txt", "w", encoding="utf-8") as f:
            f.write(timer)
        time.sleep(1)
        t -= 1

    print("Stream ended!")

t = input("Enter the time in seconds: ")

countdown(int(t))