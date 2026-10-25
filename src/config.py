import os
import json
from pathlib import Path
from dotenv import load_dotenv

USERDATA_PATH = Path(__file__).parent.parent / "userdata.json"

with USERDATA_PATH.open("r", encoding="utf-8") as file:
    userdata = json.load(file)

load_dotenv()

TWITCH_TOKEN = userdata["TWITCH_TOKEN"]
STREAMLABS_SOCKET_TOKEN = userdata["STREAMLABS_SOCKET_TOKEN"]

TWITCH_NAME = userdata["TWITCH_NAME"]
TWITCH_CHANNEL = userdata["TWITCH_CHANNEL"]

# Base values:

SECONDS_PER_SUB = int(userdata.get("SECONDS_PER_SUB", 60))
SECONDS_PER_100_BITS = int(userdata.get("SECOND_PER_100_BITS", 30))
SECONDS_PER_1_USD = int(userdata.get("SECONDS_PER_1_USD", "30"))

# Bonus time for sub bundles

BONUS_SECONDS_PER_5_SUBS = int(userdata.get("SECONDS_PER_5_SUBS", 120))
BONUS_SECONDS_PER_10_SUBS = int(userdata.get("SECONDS_PER_10_SUBS", 300))
BONUS_SECONDS_PER_20_SUBS = int(userdata.get("SECONDS_PER_20_SUBS", 600))

# Bonus time for donations

BONUS_SECONDS_PER_25_USD = int(userdata.get("SECONDS_PER_25_USD", 150))
BONUS_SECONDS_PER_100_USD = int(userdata.get("SECONDS_PER_100_USD", 600))

# Timer cap

TIMER_CAP_SECONDS = int(userdata.get("TIMER_CAP_SECONDS", 43200))