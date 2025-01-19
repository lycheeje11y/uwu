import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

EXTENSIONS = ["cogs.general", "cogs.verses", "cogs.quotes"]
