from Bots.Bot import Bot


class EasterEggBot(Bot):
    def __init__(self, message):
        super().__init__(message)

    async def talk(self):
        if self.check_content("???"):
            await self.say("Oia o bot aqui rapai, fica esperto " + self.mention)

        if self.check_content("!!!"):
            await self.react("😑")

        vessel = ["!play vessel", "-play vessel", ">play vessel"]
        for variant in vessel:
            if self.check_content_start(variant):
                await self.react("😑")
                await self.say("Carai Barba, você só ouve isso!")

        best_of = [
            "!play melhores",
            "-play melhores",
            ">play melhores",
            "!play as melhores",
            "-play as melhores",
            ">play as melhores",
        ]
        for variant in best_of:
            if self.check_content_start(variant):
                await self.react("😁")
                await self.say("Taporra, " + self.mention + " lançou a braba!")
