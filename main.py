import discord

from configs.configs import get_token
from events_handler import event_handler
from commands_handler import commands_handler

class Client(discord.Bot):
    def __init__(self, *, loop = None, **options):
        super().__init__(loop=loop, **options)
        
        event_handler(client=self)
        commands_handler(client=self)

if __name__ == "__main__":
    client = Client(intents=discord.Intents.all())
    client.run(get_token())