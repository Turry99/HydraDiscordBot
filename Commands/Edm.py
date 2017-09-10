import asyncio
import random


class Edm:
    
    async def checkCommand(self, message):
       return message.content.startswith("!edm")
           
     
    async def getName(self):
       return await  "edm"
      
      
    async def activateCommand(self, message, client):
        """
	      It will chose a random element if !rand fElem sElem
        If they are both integers , then chose a number from that range
        """
        elements = message.content.split(" ")
        
        if len(elements) > 1 and elements[1] == "help":
          return await client.send_message(message.channel, "Returns random edm meme")

        results = ['https://i.imgur.com/snbEvr8.jpg','https://i.imgur.com/b0Xo5xb.jpg']
        url = results[random.randint(0, len(results) - 1)]
        return await client.send_message(message.channel, url)
 
     