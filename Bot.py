import discord
from discord.ext import commands
import os
import random
from BotToken import token
from functions import *
from random import randint as r
game = Game()

intents = discord.Intents(messages = True, guilds= True, reactions = True, members = True, presences = True)
intents.message_content = True
Bot = commands.Bot(command_prefix="/s ", intents=intents)

@Bot.event
async def on_ready():
    print(f"{Bot.user} Ready!")
@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} Geri bas ulen !")
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="genel")
    await channel.send(f"{member} bby git !")

@Bot.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit=amount)

@Bot.command()
async def adamAs(msg):
    await msg.send("Asıldın")
@Bot.command()
async def a(msg):
    await msg.send("Ayıp")

@Bot.command(aliases=["game","oyun"])
async def haeydra(ctx, *args):
    if "zar" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send("lordun teki !")

@Bot.command()
async def king(msg):
    await msg.send("My Lord Haeydra ! ")
@Bot.command()
async def bb(msg):
    await msg.send("Bby :( ! ")



Bot.run(token)