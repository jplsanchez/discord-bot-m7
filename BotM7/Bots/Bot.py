class Bot:
    def __init__(self, message):
        self.message = message
        self.content = message.content.lower()
        self.channel = message.channel
        self.author = message.author.name
        self.author_id = message.author.id
        self.mention = message.author.mention

    def check_content(self, request):
        if self.content == request.lower():
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
        if self.content == channel.lower():
            return True
        return False
