import os
import discord
from discord.ext import commands
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
bot = commands.Bot(command_prefix='~', intents = discord.Intents.all())

@bot.command()
async def hello(ctx, arg=None):
  await ctx.send("hello! shut the fuck up!")

bot.run(token)