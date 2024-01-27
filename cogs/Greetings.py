# Contains multiple commands, events, listeners, etc.
# for command: @commands.command()
# for event: @commands.Cog.listener()

import discord
from discord import app_commands
from discord.ext import commands
from constant.messages import *
from constant.credentials import *

guild = discord.Object(id=GUILD_ID)

class Greetings(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Greeting cog loaded.')

  @app_commands.command( name="hello", description="Bot says hello to you" )
  async def hello(self, interaction: discord.Interaction):
    await interaction.response.send_message(GREETING)

async def setup(client):
  await client.add_cog(Greetings(client), guilds= [guild])