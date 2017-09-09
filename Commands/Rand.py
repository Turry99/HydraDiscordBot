import random
import asyncio

class Rand:
    
    async def checkCommand(self, message):
       return message.content.startswith("!rand")
           
     
    async def getName(self):
       return await  "rand"
      
      
    async def activateCommand(self, message, client):
        """
	      It will chose a random element if !rand fElem sElem
        If they are both integers , then chose a number from that range
        """
        elements = message.content.split(" ")
        if len(elements) == 1:
          await client.send_message(message.channel, "Invalid use of the command")
          return await client.send_message(message.channel, "Type in [!rand help] to see proper use")
        
        if elements[1] == "help":
          await client.send_message(message.channel, "Choses a random number from a range (ex: !rand 0 10)")
          return await client.send_message(message.channel, "Choses a random name from a list (atleast 2) (ex: !rand Python Tzar)")

        elif len(elements) < 2:
          return await client.send_message(message.channel, "You need atleast 2 elements.")
        else:
          try:
            #There are 2 integers
            elements[1] = int(elements[1])
            elements[2] = int(elements[2])
            chosen = random.randint(elements[1], elements[2])
            return await client.send_message(message.channel, "The number I chose is {}".format(chosen))
          except:
            #There are strings
            total = len(elements) - 1 #We substract the first element (!rand)
            chosen = random.randint(1,total)  #We add 1 so it matches the list elements
            #await client.send_message(message.channel, elements[chosen])
            return await client.send_message(message.channel, "I'm chosing {}".format(elements[chosen]))
 
     