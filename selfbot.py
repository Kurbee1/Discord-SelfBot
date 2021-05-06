import discord, json, pyfiglet

from discord.ext import commands

bot = commands.Bot(description="we do a little trolling", command_prefix="./", self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Done')

@bot.event
async def on_message(message):
    if 'RX' in message.content.lower():
        await message.channel.send('Is gay ')





with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')
bot.run(token, bot=False)
