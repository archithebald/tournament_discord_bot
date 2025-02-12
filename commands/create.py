from discord import Interaction

CATEGORY = "tournaments"

async def command(ctx: Interaction):
    print(ctx)