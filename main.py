import discord
import random
from discord.ext import commands
from BotToken import token
from functions import *
game = Game()

# Botunuzun intents'larını ayarlayın
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
intents.message_content = True

# Botunuzu oluşturun
Bot = commands.Bot(command_prefix="/", intents=intents)

# Notları saklamak için bir sözlük oluşturun
notes = {}

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
@commands.has_role("LORD")
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@Bot.command()
async def notAl(ctx, *,message):
    # Kullanıcıdan gelen notu saklayın
    notes[ctx.author.id] = message
    await ctx.send("Notunuz kaydedildi!")

@Bot.command()
async def showNote(ctx):
    # Kullanıcının kaydettiği notu alın
    note = notes.get(ctx.author.id)

    if note is not None:
        await ctx.send(f"Senin notun: {note}")
    else:
        await ctx.send("Henüz bir notunuz yok.")

@Bot.command()
async def mkt(ctx, user1: discord.User, user2: discord.User):
    # Kullanıcıları rastgele bir seçenekle eşleştirin
    choices = ["Taş", "Kağıt", "Makas"]
    choice1 = random.choice(choices)
    choice2 = random.choice(choices)

    # Sonuçları belirleyin
    result = determine_winner(choice1, choice2)

    # Sonucu mesajlaştırın
    await ctx.send(f"{user1.mention} ({choice1}) vs {user2.mention} ({choice2}) - Sonuç: {result}")

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Berabere!"
    elif (
        (choice1 == "Taş" and choice2 == "Makas")
        or (choice1 == "Makas" and choice2 == "Kağıt")
        or (choice1 == "Kağıt" and choice2 == "Taş")
    ):
        return "Kazanan: Birinci Oyuncu"
    else:
        return "Kazanan: İkinci Oyuncu"

@Bot.command()
async def zar(ctx):
    await ctx.send(game.roll_dice())

@Bot.command()
async def yazt(ctx):
    # Kullanıcıları rastgele bir seçenekle eşleştirin
    choices = ["Yazı", "Tura"]
    # Sonuçları belirleyin
    result = random.choice(choices)
    # Sonucu mesajlaştırın
    await ctx.send(f"Sonuç: {result}")

@Bot.command()
async def halay(ctx):
    await ctx.send("*¯\_(ツ)_/¯"+10*"¯\_(ツ)_/¯")

@Bot.command()
async def king(ctx):
    await ctx.send("My Lord Haeydra ! ")

@Bot.command()
async def bb(ctx):
    await ctx.send("Bby :( ! ")

Bot.run(token)
