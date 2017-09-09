import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
	print("Ne-am conectat")

@client.event
async def on_message(message):
	if message.content.startswith("!rand"):
		"""
		It will chose a random element if !rand fElem sElem
		If they are both integers , then chose a number from that range
		"""
		elements = message.content.split(" ")
		if elements[1] == "help":
			await client.send_message(message.channel, "Choses a random number from a range (ex: !rand 0 10)")
			await client.send_message(message.channel, "Choses a random name from a list (atleast 2) (ex: !rand Python Tzar)")

		elif len(elements) < 2:
			await client.send_message(message.channel, "You need atleast 2 elements.")
		try:
			#There are 2 integers
			elements[1] = int(elements[1])
			elements[2] = int(elements[2])
			chosen = random.randint(elements[1], elements[2])
			await client.send_message(message.channel, "The number I chose is {}".format(chosen))
		except:
			#There are strings
			total = len(elements) - 1 #We substract the first element (!rand)
			chosen = random.randint(1,total)  #We add 1 so it matches the list elements
			#await client.send_message(message.channel, elements[chosen])
			await client.send_message(message.channel, "I'm chosing {}".format(elements[chosen]))

client.run("<token>")
