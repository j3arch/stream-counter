import os
import asyncio
from dotenv import load_dotenv
from twitchio.ext import commands
from timer_service import countdown

def main() -> None:
    user_input = input("Enter the time in seconds: ")

    countdown(int(user_input))

if __name__ == "__main__":
    main()