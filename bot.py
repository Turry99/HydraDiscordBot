import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sys
import time


"""Set Sys path"""
sys.path.append('/home/cabox/workspace/Commands')
								
from Commands import Rand
from Commands import Tky
from Commands import Edm
from Commands import Tzar
from Commands import Doggo
from Commands import Imger
client = discord.Client()
starttime = time.time()
"""Commands you want Available"""
my_commands = [Rand(),Tky(),Edm(),Tzar(), Doggo(), Imger()]

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="with Hydrus.group"))
	print("Hydrus for the win")

	
"""On message event"""	
@client.event
async def on_message(message):
	if message.content.startswith('!'):
		for cmd in my_commands:
			if await checkActive(cmd, message):
				global starttime
				timeout = time.time() - starttime
				if timeout < 5:
					return await client.send_message(message.channel, "Timeout: wait at least 5 seconds")
				await activate(cmd, message, client)
				starttime = time.time()
				return
				
		
		
"""checks if a command was called"""		
@client.event		
async def checkActive(entity, message):
	return await entity.checkCommand(message)


"""Activates a command"""
@client.event
async def activate(entity, message, client):
	await entity.activateCommand(message, client)
	
	
"""run client on token"""
client.run("<token>")
