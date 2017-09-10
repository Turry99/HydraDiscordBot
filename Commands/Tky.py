import random
import asyncio
import os
import sys
import urllib.request
import json
import imghdr
import codecs

class Tky:
    
    async def checkCommand(self, message):
       return message.content.startswith("!tky")
           
     
    async def getName(self):
       return await  "tky"
      
      
    async def activateCommand(self, message, client):
        """
	      It will chose a random element if !rand fElem sElem
        If they are both integers , then chose a number from that range
        """
        elements = message.content.split(" ")
        
        if len(elements) > 1 and elements[1] == "help":
          return await client.send_message(message.channel, "Returns random cute anime girl image")

        f = urllib.request.urlopen('https://www.googleapis.com/customsearch/v1?key=<api_key>&cx=<custom_search_id>&q=cute%20anime%20girls&num=10')
        reader = codecs.getreader("utf-8")
        data = json.load(reader(f))
        f.close()

        results = data['items']
        url = results[random.randint(0, len(results) - 1)]['pagemap']['cse_image'][0]['src']
        return await client.send_message(message.channel, url)
 
     