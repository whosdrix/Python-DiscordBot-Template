import discord
from discord import app_commands
from discord.ext import commands

class PingCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name="ping", description="example of ping slash command")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f"Pong! {bot_latency} ms.")


async def setup(client):
    await client.add_cog(PingCommand(client))