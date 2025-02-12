import discord
import importlib

from configs.configs import get_events_files

def event_handler(client: discord.Bot):
    files = get_events_files()
    
    for file in files:
        name = file.split(".")[0]
        try: 
            module = importlib.import_module(f"events.{name}")

            client.add_listener(module.handle, f"on_{name}")
        except Exception as e:
            print(f">>>> Can't register event {name}, error: {e}")