import discord
import os
import requests
import json
from dotenv import load_dotenv

from PIL import Image, ImageDraw, ImageFont
from discord.ext.commands import bot
from discord.utils import get
from discord.ext import commands, tasks
from io import BytesIO
import random

intents = discord.Intents.default()       # Dont forget to on Privileged Gateway Intents in discord dev portal
intents.members = True
intents = intents.all()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client=commands.Bot(command_prefix="!", intents=intents)
client.remove_command('help')
status=['!helpme']

@client.event
async def on_ready():
  change_status.start()
  auto_motivate.start()
  print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds=15)
async def change_status():
  await client.change_presence(activity=discord.Game(random.choice(status)))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
      a = message.content.startswith('hello455')
      print(a)
    if message.content.startswith('fuck'):
      quote = "you have been warned "
      await message.channel.send(quote)
    if message.content.startswith('!site'):
      quote = "HackTheWorld live site - https://hacktheworld.online/"
      await message.channel.send(quote)
    if message.content.startswith('!devpost'):
      quote = "HackTheWorld Devpost - https://hacktheworld-online.devpost.com/?ref_feature=challenge&ref_medium=discover "
      await message.channel.send(quote)
    if message.content.startswith('!twitch'):
      quote = "HackTheWorld Twitch - https://www.twitch.tv/00mb1 "
      await message.channel.send(quote)  
    if message.content.startswith('!linkedin'):
      quote = "HackTheWorld LinkedIn - https://www.linkedin.com/company/neuralworks/ "
      await message.channel.send(quote)
    if message.content.startswith('!neuralworks'):
      quote = "NeuralWorks live site - https://neuralworks.group/"
      await message.channel.send(quote)
    if message.content.startswith('!helpme'):
        quote = "All commands \n !helpme \n !site - HackTheWorld Live site \n !devpost - HackTheWorld Devpost \n !twitch - HackHackTheWorld Twitch \n !linkedin - HackTheWorld LinkedIn \n !neuralworks - Neural Works Site \n !motivate - get motivational quote"
        await message.channel.send(quote)
    await client.process_commands(message)

@tasks.loop(seconds=28800)
async def auto_motivate():
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote =json_data[0]['q']
  list=quote.split()

  ran=["photo.jpg","photo2.jpg","photo3.jpg","photo4.jpg","photo5.jpg","photo6.jpg"]
  img = Image.open(random.choice(ran))
  img = img.resize((9000, 8000))

  myFont = ImageFont.truetype('PermanentMarker-Regular.ttf', 400)

  list1=list[:5]
  list2=list[5:10]
  list3=list[10:15]
  list4=list[15:]
  author= " -"+json_data[0]["a"]

  image_edit=ImageDraw.Draw(img)
  image_edit.text((600,1000)," ".join(list1),(237,230,211),font=myFont)
  image_edit.text((600,1400)," ".join(list2),(237,230,211),font=myFont)
  image_edit.text((600,1800)," ".join(list3),(237,230,211),font=myFont)
  image_edit.text((600,2200)," ".join(list4),(237,230,211),font=myFont)
  image_edit.text((900,2600),author,(237,230,211),font=myFont)
  img.save("done.jpg")

  embed = discord.Embed(title="Inspiration", color=0x00ff00) #creates embed
  file = discord.File("/home/runner/hacktheworld-bot/done.jpg", filename="done.jpg")   # set absolute path of done.jpg image from your machine
  embed.set_image(url="attachment://done.jpg")
  embed.set_footer(text="Automatic quotes for your server")

  channel = client.get_channel(845354528819118121)  # Set your channel id in which you want to send post
  await channel.send(file=file, embed=embed)
  
@client.command()
async def motivate(ctx):
  response=requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote =json_data[0]['q']
  list=quote.split()

  ran=["photo.jpg","photo2.jpg","photo3.jpg","photo4.jpg","photo5.jpg","photo6.jpg"]
  img = Image.open(random.choice(ran))
  img = img.resize((9000, 8000))

  myFont = ImageFont.truetype('PermanentMarker-Regular.ttf', 400)

  list1=list[:5]
  list2=list[5:10]
  list3=list[10:15]
  list4=list[15:]
  author= " -"+json_data[0]["a"]

  image_edit=ImageDraw.Draw(img)
  image_edit.text((600,1000)," ".join(list1),(237,230,211),font=myFont)
  image_edit.text((600,1400)," ".join(list2),(237,230,211),font=myFont)
  image_edit.text((600,1800)," ".join(list3),(237,230,211),font=myFont)
  image_edit.text((600,2200)," ".join(list4),(237,230,211),font=myFont)
  image_edit.text((900,2600),author,(237,230,211),font=myFont)

  img.save("done.jpg")

  embed = discord.Embed(title="Inspiration", color=0x00ff00) #creates embed
  file = discord.File("/home/runner/hacktheworld-bot/done.jpg", filename="done.jpg") # set absolute path of done.jpg image from your machine
  embed.set_image(url="attachment://done.jpg")
  await ctx.reply(file=file, embed=embed)

client.run(TOKEN)