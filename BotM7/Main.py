import os
import discord
import nest_asyncio

from Bot import Bot
from Conversation.Conversation import Conversation


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

nest_asyncio.apply()
client = discord.Client()

# ------------------- Main Program -------------------


@client.event
async def on_ready():
    print("INFO:\nBot Inicializado")
    print("Nome do bot: " + client.user.name)
    print("ID do bot: " + str(client.user.id))


@client.event
async def on_message(message):
    bot = Bot(message)

    if bot.author == client.user.name:
        return

    # ------------------- BOT -------------------
    talk = Conversation(bot)
    await talk.run()


client.run(DISCORD_TOKEN)
