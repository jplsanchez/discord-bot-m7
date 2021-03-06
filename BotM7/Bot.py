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

    def get_last_word_from_message(self):
        return self.message.content.split()[-1]

    def get_last_but_one_word_from_message(self):
        return self.message.content.split()[-2]

    def get_id_from_mention(self, mention):
        return mention[3:-1]
