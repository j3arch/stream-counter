import os
from dotenv import load_dotenv

load_dotenv()

TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
STREAMLABS_SOCKET_TOKEN = os.getenv("STREAMLABS_SOCKET_TOKEN")

TWITCH_NAME = os.getenv("TWITCH_NAME")
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")

SECONDS_PER_SUB = int(os.getenv("SECONDS_PER_SUB", "60"))
SECONDS_PER_100_BITS = int(os.getenv("SECOND_PER_100_BITS", "30"))

SECONDS_PER_1_USD = int(os.getenv("SECONDS_PER_1_USD", "30"))

# Custom values

SECONDS_PER_5_SUBS = int(os.getenv("SECONDS_PER_5_SUBS", "420"))
SECONDS_PER_10_SUBS = int(os.getenv("SECONDS_PER_10_SUBS", "900"))
SECONDS_PER_20_SUBS = int(os.getenv("SECONDS_PER_20_SUBS", "1800"))