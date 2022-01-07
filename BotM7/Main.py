import os
import discord
import nest_asyncio

from Data import Data
from datetime import datetime, timedelta


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

nest_asyncio.apply()
client = discord.Client()

rules = (
    "**Regras:**\n"
    + "- Cada emblema de Maestria 7 novo vale um ponto\n"
    + "- Cada emblema de Maestria 6 novo vale 0,5 ponto\n"
    + "- Pra entrar no campeonato tem que postar a foto atual dos emblemas atuais e das maestrias 7\n"
    + "- Só são contabilizados emblemas obtidos depois da adesão ao campeonato\n"
)

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

    if author == client.user.name:
        return

    # ------------------- Easter Eggs -------------------

    if content.startswith("???") and channel.name == "m7":
        await message.channel.send("Oia o bot aqui rapai, fica esperto " + mention)

    if content == "!!!":
        await message.add_reaction("😑")

    if content.startswith("!play vessel") or content.startswith(">play vessel"):
        await message.add_reaction("😑")
        await message.channel.send("Carai, " + mention + " você só ouve isso!")

    if (
        content.startswith("!play melhores")
        or content.startswith("!play as melhores")
        or content.startswith(">play as melhores")
    ):
        await message.add_reaction("😁")
        await message.channel.send("Taporra, " + mention + " lançou a braba!")

    # ------------------- BOT -------------------

    if channel.name == "m7":
        if content == "?help" or content == "?h":
            await message.channel.send(
                "**COMANDOS DO BOT**\n"
                + "**?rules :** Regras do campeonato\n"
                + "**?p :** Pontos atuais\n"
                + "**?r :** Ranking atual de jogadores\n"
                + "**?m6 :** Cadastrar emblema de Maestria 6\n"
                + "**?m7 :** Cadastrar emblema de Maestria 7\n"
                + "**?c :** Se cadastrar no campeonato"
            )
        if content == "?rules":
            Data.add_new_participant(author_id, author)

            await message.channel.send(rules)

        if content == "?c":
            Data.add_new_participant(author_id, author)

            await message.channel.send(
                mention + "cadastrado no sistema," + "aguarde sua aprovação"
            )

        if content == "?r":
            ranking = Data.get_general_ranking()
            print(ranking)
            result = ""
            for row in ranking:
                result += row[0] + " - " + str(row[1]) + " pontos\n"

            await message.channel.send(result)

        if content == "?p":
            points = Data.get_points_by_id(author_id)
            result = "{0} - {1} pontos\n".format(mention, points)

            await message.channel.send(result)

        if content == "?m6":
            if Data.has_recent_image(author_id):

                points = Data.get_points_by_id(author_id)
                points += 0.5
                Data.update_points(author_id, points)

                await message.channel.send(
                    mention
                    + " parabéns pelo Emblema M6! - Pontos totais: "
                    + str(points)
                )
            else:
                await message.channel.send(
                    "Por favor, envie a foto do emblema antes de realizar o cadastro"
                )

        if content == "?m7":
            if Data.has_recent_image(author_id):
                points = Data.get_points_by_id(author_id)
                points += 1

                Data.update_points(author_id, points)

                await message.channel.send(
                    mention
                    + " parabéns pelo Emblema M7! - Pontos totais: "
                    + str(points)
                )
            else:
                await message.channel.send(
                    "Por favor, envie a foto do emblema antes de realizar o cadastro"
                )

        if len(message.attachments) > 0:
            pic_ext = [".jpg", ".png", ".jpeg"]
            try:
                url = message.attachments[0].url
                filename = message.attachments[0].filename
                for ext in pic_ext:
                    if filename.endswith(ext):
                        Data.add_new_image(author_id, url, filename)
                        await message.channel.send("Imagem cadastrada com sucesso!")

            except:
                print(
                    "Imagem encontrada porém erro ao obter atributos tag=message_attachments"
                )


client.run(DISCORD_TOKEN)
