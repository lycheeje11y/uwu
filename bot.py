"""this is a bot"""

import discord
from discord.ext import commands

from config import TOKEN


class UwuBot(commands.Bot):
    async def setup_hook(self):
        """do stuff"""

        print(f"I am {self.user}")
        await self.load_extension("uwu")


if __name__ == "__main__":
    intents = discord.Intents.default()
    intents.message_content = True

    bot = UwuBot(intents=intents, command_prefix=";")
    bot.run(str(TOKEN))
