from pynput import keyboard
from timer_service import Timer
import asyncio

def keyboard_shortcuts_listener(timer: Timer, loop: asyncio.AbstractEventLoop) -> None:

    def on_press(key):
        try:
            if key == keyboard.Key.page_up:
                loop.call_soon_threadsafe(timer.add_seconds, 60)
                print("Manually added 60s")
            
            if key == keyboard.Key.page_down:
                loop.call_soon_threadsafe(timer.add_seconds, -60)
                print("Manually removed 60s")
        
        except AttributeError:
            pass

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        print("shortcuts active")
