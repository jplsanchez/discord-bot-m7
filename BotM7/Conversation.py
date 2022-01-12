from Bot import Bot
from Data import Data
from Enums.MessageEnum import MessageEnum
from Enums import UtilsEnum, EasterEggsEnum


class Conversation:

    bot: Bot
    DUNGEON_MASTER_ID: str

    def __init__(self, bot: Bot, master_id="359883763985022977") -> None:
        self.DUNGEON_MASTER_ID = master_id
        self.bot = bot

    async def run(self) -> None:
        await self.__default_messages()
        await self.__eater_eggs_messages()

    async def __default_messages(self):
        if self.bot.check_channel("m7"):

            if self.bot.author_id == self.DUNGEON_MASTER_ID:
                pass

            if self.bot.check_content("?help", "?h"):
                await self.bot.say(MessageEnum.COMMANDS_LIST.value)

            if self.bot.check_content("?rules"):
                Data.add_new_participant(self.bot.author_id, self.bot.author)
                await self.bot.say(MessageEnum.RULES.value)

            if self.bot.check_content("?c"):
                Data.add_new_participant(self.bot.author_id, self.bot.author)
                await self.bot.say(
                    self.bot.mention + MessageEnum.REGISTERED_SUCCESSFULLY.value
                )

            if self.bot.check_content("?r"):
                ranking = Data.get_general_ranking()
                print(ranking)
                result = ""
                for row in ranking:
                    result += f"{row[0]} - {str(row[1])} pontos\n"

                await self.bot.say(result)

            if self.bot.check_content("?rg"):
                ranking = Data.get_general_overall_ranking()
                print(ranking)
                result = MessageEnum.EVERY_SEASON_RANKING.value
                for row in ranking:
                    result += f"{row[0]} - {str(row[1])} pontos\n"

                await self.bot.say(result)

            if self.bot.check_content("?p"):
                points = Data.get_points_by_id(self.bot.author_id)
                result = f"{self.bot.mention} - {points} pontos\n"

                await self.bot.say(result)

            if self.bot.check_content("?m6"):
                if Data.has_recent_image(self.bot.author_id):
                    points = Data.get_points_by_id(self.bot.author_id)
                    points += 0.5
                    Data.update_points(self.bot.author_id, points)

                    await self.bot.say(
                        self.bot.mention + MessageEnum.M6_EMBLEM.value + str(points)
                    )
                else:
                    await self.bot.say(MessageEnum.PLEASE_SEND_PICTURE.value)

            if self.bot.check_content("?m7"):
                if Data.has_recent_image(self.bot.author_id):
                    points = Data.get_points_by_id(self.bot.author_id)
                    points += 1
                    Data.update_points(self.bot.author_id, points)

                    await self.bot.say(
                        self.bot.mention + MessageEnum.M7_EMBLEM.value + str(points)
                    )
                else:
                    await self.bot.say(MessageEnum.PLEASE_SEND_PICTURE.value)

            if len(self.bot.message.attachments) > 0:
                try:
                    url = self.bot.message.attachments[0].url
                    filename = self.bot.message.attachments[0].filename

                    for ext in UtilsEnum.image_format_list():
                        if filename.endswith(ext):
                            Data.add_new_image(self.bot.author_id, url, filename)
                            await self.bot.say(MessageEnum.IMAGE_REGISTERED.value)

                except:
                    print(
                        "ERROR: Imagem encontrada porém erro ao obter atributos tag=message_attachments"
                    )

    async def __eater_eggs_messages(self):
        if self.bot.check_content("???"):
            await self.bot.say(f"Oia o bot aqui rapai, fica esperto {self.mention}")

        if self.bot.check_content("!!!"):
            await self.bot.react("😑")

        for variant in EasterEggsEnum.VesselList():
            if self.bot.check_content_start(variant):
                await self.bot.react("😑")
                await self.bot.say("Carai Barba, você só ouve isso!")

        for variant in EasterEggsEnum.BestOfList():
            if self.bot.check_content_start(variant):
                await self.bot.react("😁")
                await self.bot.say(f"Taporra, {self.mention} lançou a braba!")
