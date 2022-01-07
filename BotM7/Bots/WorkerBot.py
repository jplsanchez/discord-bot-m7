from Bots.Bot import Bot
from Data import Data


class WorkerBot(Bot):

    rules = (
        "**Regras:**\n"
        + "- Cada emblema de Maestria 7 novo vale um ponto\n"
        + "- Cada emblema de Maestria 6 novo vale 0,5 ponto\n"
        + "- Pra entrar no campeonato tem que postar a foto atual dos emblemas atuais e das maestrias 7\n"
        + "- Só são contabilizados emblemas obtidos depois da adesão ao campeonato\n"
    )

    def __init__(self, message):
        super().__init__(message)

    async def commands(self):
        if self.content == "?help" or self.content == "?h":
            await self.message.channel.send(
                "**COMANDOS DO BOT**\n"
                + "**?rules :** Regras do campeonato\n"
                + "**?p :** Pontos atuais\n"
                + "**?r :** Ranking atual de jogadores\n"
                + "**?m6 :** Cadastrar emblema de Maestria 6\n"
                + "**?m7 :** Cadastrar emblema de Maestria 7\n"
                + "**?c :** Se cadastrar no campeonato"
            )
        if self.content == "?rules":
            Data.add_new_participant(self.author_id, self.author)

            await self.message.channel.send(self.rules)

        if self.content == "?c":
            Data.add_new_participant(self.author_id, self.author)

            await self.message.channel.send(
                self.mention + "cadastrado no sistema," + "aguarde sua aprovação"
            )

        if self.content == "?r":
            ranking = Data.get_general_ranking()
            print(ranking)
            result = ""
            for row in ranking:
                result += row[0] + " - " + str(row[1]) + " pontos\n"

            await self.message.channel.send(result)

        if self.content == "?p":
            points = Data.get_points_by_id(self.author_id)
            result = "{0} - {1} pontos\n".format(self.mention, points)

            await self.message.channel.send(result)

        if self.content == "?m6":
            if Data.has_recent_image(self.author_id):

                points = Data.get_points_by_id(self.author_id)
                points += 0.5
                Data.update_points(self.author_id, points)

                await self.message.channel.send(
                    self.mention
                    + " parabéns pelo Emblema M6! - Pontos totais: "
                    + str(points)
                )
            else:
                await self.message.channel.send(
                    "Por favor, envie a foto do emblema antes de realizar o cadastro"
                )

        if self.content == "?m7":
            if Data.has_recent_image(self.author_id):
                points = Data.get_points_by_id(self.author_id)
                points += 1

                Data.update_points(self.author_id, points)

                await self.message.channel.send(
                    self.mention
                    + " parabéns pelo Emblema M7! - Pontos totais: "
                    + str(points)
                )
            else:
                await self.message.channel.send(
                    "Por favor, envie a foto do emblema antes de realizar o cadastro"
                )

        if len(self.message.attachments) > 0:
            pic_ext = [".jpg", ".png", ".jpeg"]
            try:
                url = self.message.attachments[0].url
                filename = self.message.attachments[0].filename
                for ext in pic_ext:
                    if filename.endswith(ext):
                        Data.add_new_image(self.author_id, url, filename)
                        await self.message.channel.send("Imagem cadastrada com sucesso!")

            except:
                print(
                    "Imagem encontrada porém erro ao obter atributos tag=message_attachments"
                )