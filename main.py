import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.all()

bot = commands.Bot(command_prefix='!helloworld', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')

@bot.command(name='hi')
async def hi(ctx):
    await ctx.send('Hi!')
bot.run('MTE5MjI3MjIxNTIwMzM4MTI4MA.Gl43tB.OJuXmC7iiB_2QRRaZbmIAVhlaqd9Q1kGKa8pp8')
