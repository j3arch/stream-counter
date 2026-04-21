import keyboard
from timer_service import Timer
import asyncio

def keyboard_shortcuts_listener(timer: Timer, loop: asyncio.AbstractEventLoop) -> None:

    keyboard.add_hotkey("F12", lambda: loop.call_soon_threadsafe(timer.add_seconds, 60))
    print("keyboard shortcut added 60 seconds")