import asyncio
import time
import requests
import os
from PIL import Image, ImageFilter

class Imger:

  async def checkCommand(self, message):
    return message.content.startswith('!imgm')
  async def getName(self):
    return await "imgm"
  async def activateCommand(self, message, client):
    helpmessage = message.author.mention + "```Correct Usage: !imgm <file> OR !imgm <link>```"
    #HTTPs/Sent file only support.
    elements = message.content.split(" ")
    if not message.attachments:
      if elements[1][:5] == "https":
        #User is trying to send a link
        imageurl = elements[1]
        if imageurl[-4:] != ".jpg" and imageurl[-4:] != ".png":
          filename = message.author.id + ".jpg"
        else:
          filename = message.author.id + imageurl[-4:]
        theimage = requests.get(imageurl).content
        with open(filename, 'wb') as outputimg:
          outputimg.write(theimage)
        #Image saved to filename
        imgmanipulation = Image.open(filename)
        sharpimage = imgmanipulation.filter(ImageFilter.CONTOUR)
        savename = "save" + filename
        sharpimage.save(savename)
        #File saved send it in discord
        await client.send_message(message.channel, message.author.mention)
        await client.send_file(message.channel, savename)
        #Done with both files delete:
        os.remove(filename)
        os.remove(savename)
      else:
        newmsg = helpmessage + "Notes: I only accept HTTPS links, sorry!"
        return await client.send_message(message.channel, newmsg)
    else:
      attachments = message.attachments
      if not attachments:
        return await client.send_message(message.channel, helpmessage)
      else:
        filename = message.author.id + attachments[0]['url'][-4:]
        userimage = requests.get(attachments[0]['url']).content
        with open(filename, 'wb') as outputimg:
          outputimg.write(userimage)
        #Downloaded original image now manipulate it!
        imgmanipulation = Image.open(filename)
        sharpimage = imgmanipulation.filter(ImageFilter.CONTOUR)
        savename = "save" + filename
        sharpimage.save(savename)
        await client.send_message(message.channel, message.author.mention)
        await client.send_file(message.channel, savename)
        #File is sent delete both new and old image
        os.remove(savename)
        os.remove(filename)    
