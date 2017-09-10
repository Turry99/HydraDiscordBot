import random
import asyncio
import urllib.request
import json
import imghdr
import codecs
import discord
from discord.ext.commands import Bot
from discord.ext import commands
#Find and post a picture of a random dog :)
class Doggo:
 async def checkCommand(self, message):
  return message.content.startswith("!goodboy")

 async def getName(self):
  return await "goodboy"

 async def activateCommand(self, message, client):
  elements = message.content.split(" ")
  if len(elements) > 1 and elements[1] == "help":
   return await client.send_message(message.channel, "Find a random good doggo :)")
  f = urllib.request.urlopen('https://www.googleapis.com/customsearch/v1?key=<api_key>&cx=<custom_engine_id>&q=cute%20doggo&num=10')
  reader = codecs.getreader("utf-8")
  data = json.load(reader(f))
  f.close()
  results = data['items']
  murl = results[random.randint(0, len(results) - 1)]['pagemap']['imageobject'][0]['contenturl']
  usertitle = "<@"+message.author.id+">"
  await client.send_message(message.channel, usertitle)
  myMessage=discord.Embed(title="Very Cute Doggo", url=murl, color=0x0743de)
  myMessage.set_author(name="Hydrus.group", url='https://hydrus.group', icon_url=murl)
  myMessage.set_image(url=murl)
  await client.send_message(message.channel, embed=myMessage)

#Was using imgur for custom engine, but if you know other sites please use/add :)