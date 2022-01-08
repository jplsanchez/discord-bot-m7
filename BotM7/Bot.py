class Bot:
    def __init__(self, message):
        self.message = message
        self.content = message.content.lower()
        self.channel = message.channel
        self.author = message.author.name
        self.author_id = message.author.id
        self.mention = message.author.mention

    def check_content(self, *requests):
        for request in requests:
            if self.content == request.lower():
                print("INFO: Comando encontrado: " + request)
                return True
        return False

    def check_content_start(self, request):
        if self.content.startswith(request.lower()):
            return True
        return False

    async def say(self, answer):
        await self.message.channel.send(answer)

    async def react(self, reaction):
        await self.message.add_reaction(reaction)

    def check_channel(self, channel):
        if self.channel.name == channel.lower():
            return True
        return False

    async def easter_egg_talk(self):
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
