import asyncio
from timer_service import Timer, run_timer
from socket_service import streamlabs_event_listener
from shortcut_service import keyboard_shortcuts_listener, terminal_controller

async def main() -> None:
    initial_time = 7200
    shared_timer = Timer(initial_time)
    shared_timer.load_state()
    loop = asyncio.get_running_loop()
    print("Input 'start' to start the stream")

    keyboard_shortcuts_listener(shared_timer, loop)

    await asyncio.gather(
        run_timer(shared_timer),
        streamlabs_event_listener(shared_timer),
        terminal_controller(shared_timer),
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, asyncio.CancelledError):
        print("\nStream ended!")