import discord
import os
import requests
import json
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="$")


@bot.command(
    help="A simple marco-polo echo test to see if the bot is alive.",
    brief="Say marco, hear polo!"
)
async def marco(ctx):
    await ctx.channel.send("polo")

@bot.command(
    help="Echos your message in chat",
    brief="Repeats your message"
)
async def print(ctx, *msg):
    response = ""
    for arg in msg:
        response += arg + ' '
    await ctx.channel.send(response)


@bot.event
async def on_message(message):
    if message.content == "hello":
        await message.channel.send("sup how u doin")

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)