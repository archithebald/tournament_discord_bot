import discord, importlib

from discord import Interaction
from discord import application_command

from configs.configs import get_commands_files, get_command

def command_exists(client: discord.Bot, name):   
    return True if name in client.commands else False

def register_command(client: discord.Bot, command_info, module):
    name = command_info["name"]
    if command_exists(client, name):
        print(f"Command {name} exists")
    else:
        print(f"Registering command {name}")
        @client.command(name=name, description=command_info["description"])
        async def command(ctx):
            await module.command(ctx)   

def commands_handler(client: discord.Bot):
    files = get_commands_files()
    
    for file in files:
        name = file.split(".")[0]
                
        try:
            module = importlib.import_module(f"commands.{name}")

            category = module.CATEGORY
            command = get_command(category, name)
            
            register_command(client, command, module)
        except Exception as e:
            print(f">>>> Can't register command {name}, error: {e}")
            
