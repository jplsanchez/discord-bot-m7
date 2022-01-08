import os
import discord
import nest_asyncio
from dataclasses import dataclass

from Bot import Bot
from Conversation.Conversation import Conversation


@dataclass
class Configuration:
    DISCORD_TOKEN: str
    client: discord.Client


def setup() -> Configuration:
    nest_asyncio.apply()
    discord_token = os.environ.get("DISCORD_TOKEN")
    discord_client = discord.Client()

    return Configuration(discord_token, discord_client)


def main(config: Configuration):
    client = config.client

    @config.client.event
    async def on_ready():
        print("INFO:\nBot Inicializado")
        print("Nome do bot: " + config.client.user.name)

    @config.client.event
    async def on_message(message):
        bot = Bot(message)

        if bot.author == config.client.user.name:
            return

        talk = Conversation(bot)
        await talk.run()

    config.client.run(config.DISCORD_TOKEN)


if __name__ == "__main__":
    config = setup()
    main(config)
