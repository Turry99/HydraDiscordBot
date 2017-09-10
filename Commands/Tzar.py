import random
import asyncio
import time


class Tzar:
  
    def __init__(self):
       self.starttime = time.time()
    
    
    async def checkCommand(self, message):
       return message.content.startswith("!tzar")
           
     
    async def getName(self):
       return await  "tzar"
      
      
    async def activateCommand(self, message, client):
        timeout = time.time() - self.starttime
        if timeout < 600:
          return await client.send_message(message.channel, "Timeout: this command has a 10 minute cooldown")
        self.starttime = time.time()  
        allcoders = [] #List to be filled with members of coding
        tStatus = None #Empty string to be set later (Tzar's Status)
        for server in client.servers: 
            for member in server.members:
                if member.name == "Tzar": #Is the Member Tzar?
                    if str(member.status) == "online": #Is Tzar online?
                        tStatus = "online"
                        sendable = "<@"+str(member.id) + "> is online! Wake up Cuck!"
                        await client.send_message(message.channel, sendable)
                    elif str(member.status) == "dnd": #Is Tzar DnD?
                        tStatus = "dnd"
                    elif str(member.status) == "idle": #Is Tzar Idle?
                        tStatus = "idle"
                    else:
                        #Tzar is not online set a bool var for later use
                        tStatus = "offline"
                        tId = member.id
                else:
                    #They are not Tzar are they a coder?  
                    #We're online looking for coders who are online!
                    if str(member.status) == "online":     
                        rolelist = member.roles
                        for role in rolelist:
                            if role.name == "Coding":
                                #Add their user ID to list of coders for mention later
                                allcoders.append(member.id)
        if tStatus == "offline":
            #Tzar isn't online let's respond as so!
            if not allcoders:
                sendable = "<@" + tId + "> isn't online AND no coders are :("
                await client.send_message(message.channel, sendable)
            else:
                sendable = "<@" + tId + "> isn't online :/, but you can ask his favorite coder <@" + allcoders[random.randint(0, len(allcoders) -1)] + ">!"
                await client.send_message(message.channel, sendable)
        elif tStatus == "dnd":
                #Tzar is online, but DND is on so let's not bother :)
                sendable = "Tzar is busy (So we won't mention him), but you can ask his favorite coder <@" + allcoders[random.randint(0, len(allcoders)-1)] + ">!"
                await client.send_message(message.channel, sendable)
        elif tStatus == "idle":
                #Tzar is idle
                sendable = "Tzar is currently watching pornhub, we'll leave him be. " + "you can ask his favorite coder <@" + allcoders[random.randint(0, len(allcoders)-1)] + ">"
                await client.send_message(message.channel, sendable)
        else:
                #Tzar is invisible or some other state that we don't know :/
                sendable = "I don't know what Tzar is doing...sorry master. You can still ask a coder though <@" + allcoders[random.randint(0, len(allcoders)-1)] + ">"
                await client.send_message(message.channel, sendable)