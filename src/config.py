import os
from dotenv import load_dotenv

load_dotenv

SECONDS_PER_SUB = int(os.getenv("SECONDS_PER_SUB", "60"))
SECONDS_PER_100_BITS = int(os.getenv("SECOND_PER_100_BITS", "30"))