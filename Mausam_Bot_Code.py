import discord
#connection to the discord server 
import os
import requests
import json
from keep_alive import keep_alive

client=discord.Client()
def get_weather(city):
  api_address='https://api.openweathermap.org/data/2.5/weather?q='
  url=api_address+city+'&appid=fbe3bb1e18155e9596f394a5fc66e970'
  json_data=requests.get(url).json()
  name="Place: "+json_data["name"]
  main="Main: "+json_data["weather"][0]["main"]
  description="Description: "+json_data["weather"][0]["description"]
  teperature="Temperature: "+str(json_data["main"]["temp"])
  pressure="Pressure: "+str(json_data["main"]["pressure"])
  humid="Humid: "+str(json_data["main"]["humidity"])
  return(name,main,description,teperature,pressure,humid)

@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg.startswith("/check"):
    place=msg.split("/check ",1)[1]
    name,main,description,teperature,pressure,humid = get_weather(place)
    await message.channel.send(name+"\n"+main+"\n"+description+"\n"+teperature+"\n"+pressure+"\n"+humid)
    
keep_alive()

client.run(os.getenv('TOKEN'))
