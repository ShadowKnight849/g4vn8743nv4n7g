import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

botVersion = 0.1
# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Testing 123!", command_prefix="!", pm_help = True)

#Test Code
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {} |Current Bot Version: {}'.format(discord.__version__, platform.python_version(), str(botVersion)))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")

tokenFile = open("../Token.txt")
client.run(tokenFile.read())
tokenFile.close()
