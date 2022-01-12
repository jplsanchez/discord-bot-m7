from Bot import Bot
from Data import Data
from Enums.MessageEnum import MessageEnum
from Enums import UtilsEnum, EasterEggsEnum


class Conversation:

    bot: Bot
    DUNGEON_MASTER_ID: str

    def __init__(self, bot: Bot, master_id: str = "359883763985022977") -> None:
        self.DUNGEON_MASTER_ID = master_id
        self.bot = bot

    async def run(self) -> None:
        await self.__default_messages()
        await self.__eater_eggs_messages()

    async def __default_messages(self):
        if self.bot.check_channel("m7"):

            if str(self.bot.author_id) == self.DUNGEON_MASTER_ID:
                await self.__set_points()

            await self.__help_message()

            await self.__rules_message()

            await self.__sign_in_message()

            await self.__general_ranking_message()

            await self.__overall_general_ranking_message()

            await self.__individual_points_message()

            await self.__register_m6()

            await self.__register_m7()

            await self.__get_image()

    async def __set_points(self):
        if self.bot.check_content_start("?setpoints"):
            try:
                mention = self.bot.get_last_but_one_word_from_message()
                id = self.bot.get_id_from_mention(mention)
                points = float(self.bot.get_last_word_from_message())
                Data.set_points(id, points)
                await self.bot.say(MessageEnum.SET_POINTS_MESSAGE.value)
            except:
                await self.bot.say(MessageEnum.ERROR_SET_POINTS.value)

    async def __get_image(self):
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

    async def __register_m7(self):
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

    async def __register_m6(self):
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

    async def __individual_points_message(self):
        if self.bot.check_content("?p"):
            points = Data.get_points_by_id(self.bot.author_id)
            result = f"{self.bot.mention} - {points} pontos\n"

            await self.bot.say(result)

    async def __overall_general_ranking_message(self):
        if self.bot.check_content("?rg"):
            ranking = Data.get_general_overall_ranking()
            print(ranking)
            result = MessageEnum.EVERY_SEASON_RANKING.value
            for row in ranking:
                result += f"{row[0]} - {str(row[1])} pontos\n"

            await self.bot.say(result)

    async def __general_ranking_message(self):
        if self.bot.check_content("?r"):
            ranking = Data.get_general_ranking()
            print(ranking)
            result = ""
            for row in ranking:
                result += f"{row[0]} - {str(row[1])} pontos\n"

            await self.bot.say(result)

    async def __sign_in_message(self):
        if self.bot.check_content("?c"):
            Data.add_new_participant(self.bot.author_id, self.bot.author)
            await self.bot.say(
                self.bot.mention + MessageEnum.REGISTERED_SUCCESSFULLY.value
            )

    async def __rules_message(self):
        if self.bot.check_content("?rules"):
            Data.add_new_participant(self.bot.author_id, self.bot.author)
            await self.bot.say(MessageEnum.RULES.value)

    async def __help_message(self):
        if self.bot.check_content("?help", "?h"):
            await self.bot.say(MessageEnum.COMMANDS_LIST.value)

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
