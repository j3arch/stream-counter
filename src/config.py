import os
from dotenv import load_dotenv

load_dotenv()

TWITCH_TOKEN = os.getenv("TWITCH_TOKEN")
STREAMLABS_SOCKET_TOKEN = os.getenv("STREAMLABS_SOCKET_TOKEN")

TWITCH_NAME = os.getenv("TWITCH_NAME")
TWITCH_CHANNEL = os.getenv("TWITCH_CHANNEL")

# Base values:

SECONDS_PER_SUB = int(os.getenv("SECONDS_PER_SUB", "60"))
SECONDS_PER_100_BITS = int(os.getenv("SECOND_PER_100_BITS", "30"))
SECONDS_PER_1_USD = int(os.getenv("SECONDS_PER_1_USD", "30"))

# Bonus time for sub bundles

BONUS_SECONDS_PER_5_SUBS = int(os.getenv("SECONDS_PER_5_SUBS", "120"))
BONUS_SECONDS_PER_10_SUBS = int(os.getenv("SECONDS_PER_10_SUBS", "300"))
BONUS_SECONDS_PER_20_SUBS = int(os.getenv("SECONDS_PER_20_SUBS", "600"))

# Custom donation values:

SECONDS_PER_10_USD = int(os.getenv("SECONDS_PER_10_USD", "300"))
SECONDS_PER_25_USD = int(os.getenv("SECONDS_PER_25_USD", "900"))
SECONDS_PER_100_USD = int(os.getenv("SECONDS_PER_100_USD", "3600"))