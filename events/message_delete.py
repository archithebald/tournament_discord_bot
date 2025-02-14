from discord.message import Message
from configs.configs import get_channel_id

async def handle(message: Message):
    logs_id = get_channel_id("logs")
    channel = await message.guild.fetch_channel(logs_id)
    msg = f"**{message.author.display_name}/{message.author.name}** - {message.content}"
    await channel.send(msg)