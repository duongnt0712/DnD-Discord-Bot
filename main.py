import os
import asyncio
import discord
from discord.ext import commands
from constant.credentials import *
from constant.messages import *
from rest.api import *

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)

# Event
@client.event
async def on_ready():
  print("Bot is now ready for use!")
  print("---------------------------------------------")

@client.command(name="sync")
async def sync(ctx):
  synced = await client.tree.sync(guild=ctx.guild)
  await ctx.send(f"Synced {len(synced)} command(s).")

# Load cogs
async def load():
  for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
  async with client:
    await load()
    await client.start(BOT_TOKEN)

# Run client
asyncio.run(main())

