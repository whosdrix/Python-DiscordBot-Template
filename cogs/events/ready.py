import discord
from discord.ext import commands

class ReadyEvent(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        sync = await self.client.tree.sync()
        print(f"bot logged as {self.client.user}")
        print(f'synced {len(sync)} commands')

async def setup(client):
    await client.add_cog(ReadyEvent(client))