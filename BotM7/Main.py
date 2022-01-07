import os
import discord
import nest_asyncio
from MessageEnum import MessageEnum

from Bot import Bot
from Data import Data


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

nest_asyncio.apply()
client = discord.Client()

# ------------------- Main Program -------------------


@client.event
async def on_ready():
    print("Bot Iniciacado")
    print("Nome do bot: " + client.user.name)
    print("ID do bot: " + str(client.user.id))


@client.event
async def on_message(message):
    content = message.content.lower()
    channel = message.channel
    author = message.author.name
    author_id = message.author.id
    mention = message.author.mention

    bot = Bot(message)

    if author == client.user.name:
        return

    # ------------------- Easter Eggs -------------------

    await bot.easter_egg_talk()

    # ------------------- BOT -------------------

    if channel.name == "m7":
        if author_id == "359883763985022977":
            pass

        if content == "?help" or content == "?h":
            await bot.say(MessageEnum.COMMANDS_LIST.value)

        if content == "?rules":
            Data.add_new_participant(author_id, author)
            await bot.say(MessageEnum.RULES.value)

        if content == "?c":
            Data.add_new_participant(author_id, author)
            await bot.say(mention + MessageEnum.REGISTERED_SUCCESSFULLY.value)

        if content == "?r":
            ranking = Data.get_general_ranking()
            print(ranking)
            result = ""
            for row in ranking:
                result += row[0] + " - " + str(row[1]) + " pontos\n"

            await bot.say(result)

        if content == "?rg":
            ranking = Data.get_general_overall_ranking()
            print(ranking)
            result = MessageEnum.EVERY_SEASON_RANKING.value
            for row in ranking:
                result += row[0] + " - " + str(row[1]) + " pontos\n"

            await bot.say(result)

        if content == "?p":
            points = Data.get_points_by_id(author_id)
            result = "{0} - {1} pontos\n".format(mention, points)

            await bot.say(result)

        if content == "?m6":
            if Data.has_recent_image(author_id):
                points = Data.get_points_by_id(author_id)
                points += 0.5
                Data.update_points(author_id, points)

                await bot.say(mention + MessageEnum.M6_EMBLEM.value + str(points))
            else:
                await bot.say(MessageEnum.PLEASE_SEND_PICTURE.value)

        if content == "?m7":
            if Data.has_recent_image(author_id):
                points = Data.get_points_by_id(author_id)
                points += 1
                Data.update_points(author_id, points)

                await bot.say(mention + MessageEnum.M7_EMBLEM.value + str(points))
            else:
                await bot.say(MessageEnum.PLEASE_SEND_PICTURE.value)

        if len(message.attachments) > 0:
            pic_ext = [".jpg", ".png", ".jpeg"]
            try:
                url = message.attachments[0].url
                filename = message.attachments[0].filename
                for ext in pic_ext:
                    if filename.endswith(ext):
                        Data.add_new_image(author_id, url, filename)
                        await bot.say(MessageEnum.IMAGE_REGISTERED.value)

            except:
                print(
                    "ERROR: Imagem encontrada porém erro ao obter atributos tag=message_attachments"
                )


client.run(DISCORD_TOKEN)
