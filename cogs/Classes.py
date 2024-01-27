import discord
from discord import app_commands
from discord.ext import commands
from constant.messages import *
from constant.credentials import *
from rest.api import *

guild = discord.Object(id=GUILD_ID)

class Classes(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Classes cog loaded.')

  @app_commands.command( name="count_classes", description="The number of classes in game" )
  async def count_classes(self, interaction: discord.Interaction):
    response = res_count_classes()
    await interaction.response.send_message(COUNT_CLASSES.format(response))

  @app_commands.command( name="get_all_classes", description="Return all classes name" )
  async def get_all_classes(self, interaction: discord.Interaction):
    response = res_get_all_classes()
    await interaction.response.send_message(LIST_CLASSES.format(response))

async def setup(client):
  await client.add_cog(Classes(client), guilds= [guild])