import yaml, os

from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

ROOT = os.getcwd()
CONFIGS = os.path.join(ROOT, "configs")

commands = yaml.safe_load(open(os.path.join(CONFIGS, "commands.yaml")))
roles = yaml.safe_load(open(os.path.join(CONFIGS, "roles.yaml")))
channels = yaml.safe_load(open(os.path.join(CONFIGS, "channels.yaml")))

def get_commands(category: str = ""):
    return commands[category] if category != "" else commands

def get_command(category: str, name: str):
    return commands[category][name]

def get_roles():
    return roles

def get_role(name: str):
    return roles[name]

def get_token():
    return os.environ.get("TOKEN")

def get_events_files():
    EVENTS = Path(os.path.join(ROOT, "events"))
    
    files = [file.name for file in EVENTS.iterdir() if file.name.endswith(".py")]
    
    return files

def get_commands_files():
    COMMANDS = Path(os.path.join(ROOT, "commands"))
    
    files = [file.name for file in COMMANDS.iterdir() if file.name.endswith(".py")]
    
    return files

def get_channel_id(name):
    return str(channels[name]["id"])

def get_command_options(category, name):
    return commands[category][name]["options"]