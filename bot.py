import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sys

"""Set Sys path"""
sys.path.append('/home/cabox/workspace/Commands')
								
from Commands import Rand

client = discord.Client()

"""Commands you want Available"""
my_commands = [Rand()]

@client.event
async def on_ready():
	print("Hydrus for the win")

	
"""On message event"""	
@client.event
async def on_message(message):
	if message.content.startswith('!'):
		for cmd in my_commands:
			if await checkActive(cmd, message):
				await activate(cmd, message, client)
				break
		
		
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
