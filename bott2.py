import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.command()
async def hello(ctx):
    await ctx.send('ohayo')
@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency*1000)}ms')
@client.command()
async def pfp(ctx):
    m=ctx.message.author
    av=m.avatar_url
    await ctx.send(av)
@client.command()
async def cy(ctx):
    await ctx.send("https://meet.google.com/ppq-tgke-zor")
@client.command()
async def py(ctx):
    await ctx.send("https://meet.google.com/toh-wmmy-rjp")
@client.command()
async def ss(ctx):
    await ctx.send("https://meet.google.com/sbc-xibm-cbm")
@client.command()
async def clr(ctx,amount=3):
    await ctx.channel.purge(limit=amount)

@client.command()
async def candace(ctx):
    await ctx.send("lolol")
@client.command()
async def fairy(ctx):
    await ctx.send("cute")
@client.command()
async def Z(ctx):
    await ctx.send("!!!")
@client.command()
async def doomah(ctx):
    await ctx.send("ded")
client.run('ODUyNjIyMzQwNjA4MzYwNDQ4.YMJgbg.g7XhAhaGrHz2MDS8jD5J8-9nPSY')
