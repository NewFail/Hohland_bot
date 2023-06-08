import disnake
import asyncio
import os
from disnake.ext import commands
from chat_gpt import request
from app.config_reader import load_config

configs = load_config("config/bot.ini")

token=configs.DC_bot.token

config = {
    'token': token,
    'prefix': '>',
}


bot = commands.Bot(command_prefix=config['prefix'], help_command=None, intents = disnake.Intents.all())


@bot.command()
async def restart(ctx):
    os.system('start bot.exe')

@bot.command()
async def chat_gpt(ctx):
    await ctx.send("Чем вам помочь?")
    try:
                
        message = await bot.wait_for('message', timeout=60.0, check=lambda msg: msg.author == ctx.author)
        Message = message.content
        reply = request(Message)
        #print(Message)
        await ctx.reply(reply)
    except asyncio.TimeoutError:
        await ctx.send('Время вышло, жду сообщение от тебя до следующего раза.')


bot.run('MTExNjM3OTQxMTY2MzU2ODk3Nw.GRMRXy.1j885BcAfqXuqpwgGWSpPGiFNXVAlMVYGsaIwc')


