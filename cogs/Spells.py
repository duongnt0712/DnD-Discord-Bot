import discord
from discord import app_commands
from discord.ext import commands
from constant.messages import *
from constant.credentials import *
from rest.api import *

guild = discord.Object(id=GUILD_ID)

class Spells(commands.Cog):
  def __init__(self, client: commands.Bot):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print('Spells cog loaded.')

  @app_commands.command( name="get_specific_spell", description="Get a specific spell's detail." )
  async def get_specific_spell(self, interaction: discord.Interaction, spell: str):
    response = res_get_specific_spells(spell)
    embed = discord.Embed( title=response["name"])
    embed.set_thumbnail(url="https://solastacrownofthemagister.wiki.fextralife.com/file/Solasta-Crown-of-the-Magister/acid-arrow-spells-solasta-wiki-guide.png")
    embed.add_field(name="Description", value=response["desc"], inline=False)
    if response["higher_level"]:
      embed.add_field(name="Higher Level", value=response["higher_level"], inline=False)
    embed.add_field(name="Range", value=response["range"], inline=False)
    embed.add_field(name="Components", value=response["components"], inline=False)
    embed.add_field(name="Material", value=response["material"], inline=False)
    embed.add_field(name="Ritual", value=response["ritual"], inline=False)
    embed.add_field(name="Duration", value=response["duration"], inline=False)
    embed.add_field(name="Concentration", value=response["concentration"], inline=False)
    embed.add_field(name="Casting Time", value=response["casting_time"], inline=False)
    embed.add_field(name="Level", value=response["level"], inline=False)
    if response["attack_type"]:
      embed.add_field(name="Attack Type", value=response["attack_type"], inline=False)
    await interaction.response.send_message(embed=embed)

async def setup(client):
  await client.add_cog(Spells(client), guilds= [guild])