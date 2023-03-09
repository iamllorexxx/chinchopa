import discord
from discord.ext import commands
from config import settings
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()

async def hello(ctx): 
    author = ctx.message.author 

    await ctx.send(f'Привет, {author.mention}!')
async def hello(ctx): 
    author = ctx.message.author 

    await ctx.send(f'Пока, {author.mention}!')
bot.run(settings['token'])
