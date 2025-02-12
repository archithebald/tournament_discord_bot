from discord.message import Message

async def handle(message: Message):
    print(message.content)