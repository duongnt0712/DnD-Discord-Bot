import discord
from discord import app_commands
from discord.ext import commands
from constant.messages import *
from constant.credentials import *
from rest.api import *

guild = discord.Object(id=GUILD_ID)

class Subclasses(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Subclasses cog loaded.')

  @app_commands.command( name="count_subclasses", description="The number of subclasses in game" )
  async def count_subclasses(self, interaction: discord.Interaction):
    response = res_count_subclasses()
    await interaction.response.send_message(COUNT_SUBCLASSES.format(response))

  @app_commands.command( name="get_all_subclasses", description="Return all subclasses name" )
  async def get_all_subclasses(self, interaction: discord.Interaction):
    response = res_get_all_subclasses()
    await interaction.response.send_message(LIST_SUBCLASSES.format(response))

async def setup(client):
  await client.add_cog(Subclasses(client), guilds= [guild])