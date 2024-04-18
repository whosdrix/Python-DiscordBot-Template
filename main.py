import asyncio
import discord
import os
from discord.ext import commands
import json

with open("config.json") as f:
    config = json.load(f)

client = commands.Bot(command_prefix='+', intents=discord.Intents.all(), application_id=config["ClientID"])

async def setup_hook():
    # LOAD EVENT COGS
    for filename in os.listdir('./cogs/events'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.events.{filename[:-3]}')
    # LOAD COMMAND COGS
    for filename in os.listdir('./cogs/commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.commands.{filename[:-3]}')

async def main():
    await setup_hook()
    await client.start(config["Token"])

if __name__ == "__main__":
    asyncio.run(main())
