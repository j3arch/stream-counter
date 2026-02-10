import time

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