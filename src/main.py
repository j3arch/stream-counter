import os
import asyncio
from dotenv import load_dotenv
from twitchio.ext import commands
from timer_service import Timer
from timer_service import countdown

async def main():
    user_input = input("Enter the time in seconds: ")

    countdown(int(user_input))

if __name__ == "__main__":
    asyncio.run(main())