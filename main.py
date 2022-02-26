print('Fortnite-Api-Discord | Made by Th3DryZ69')
import json

############################################################################################################################################################

def data():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def text():
    try:
        with open(f'Langue/{data()["bot_lang"]}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        print('Invalid lang in settings')
        exit()

############################################################################################################################################################

try:
    from discord.ext import commands, tasks
    from discord_slash import SlashCommand, SlashContext
    from threading import Thread
    from flask import Flask
    import os
    import asyncio
    import random
    import discord
    import ast
    import inspect
    import requests
    import re
except:
    print(text()['module_not_found_error'])
    exit()

############################################################################################################################################################

intents = discord.Intents().all()
intents.members = True
bot = commands.Bot(command_prefix = data()['Prefix'], description = "GameMan_666", intents=intents)
bot.remove_command("help")
#defining stuff lol
footertext = "made with ❤"
slash = SlashCommand(bot, sync_commands=True)

#things for the commands to work

footertext = "made with ❤" #embed footer text
color = 0x5865F2     #embed color (blurple)
fortnite_api_io_key = data()["fnio"] #put it in env
bs = "<:battlestar:947252174650495016>" #put a custom battle star emoji or a star emoji to work

############################################################################################################################################################

#for cogpath in os.listdir("Fortnite/cogs"):
    #try:
        #if cogpath.endswith(".py"):
            #bot.load_extension(f'Fortnite.cogs.{cogpath[:-3]}')
            #print(f'Loaded {cogpath}')
    #except Exception as ex:
        #print(f'Something wen\'t wrong while loading {cogpath}\nError: {ex}\n\n')

############################################################################################################################################################

#for cogpath in os.listdir("Fortnite/Shop"):
    #try:
        #if cogpath.endswith(".py"):
            #bot.load_extension(f'Fortnite.Shop.{cogpath[:-3]}')
            #print(f'Loaded {cogpath}')
    #except Exception as ex:
        #print(f'Something wen\'t wrong while loading {cogpath}\nError: {ex}\n\n')

############################################################################################################################################################

for cogpath in os.listdir("Commands"):
    try:
        if cogpath.endswith(".py"):
            bot.load_extension(f'Commands.{cogpath[:-3]}')
            print(f'Loaded {cogpath}')
    except Exception as ex:
        print(f'Something wen\'t wrong while loading {cogpath}\nError: {ex}\n\n')

############################################################################################################################################################

for cogpath in os.listdir("Welcome"):
    try:
        if cogpath.endswith(".py"):
            bot.load_extension(f'Welcome.{cogpath[:-3]}')
            print(f'Loaded {cogpath}')
    except Exception as ex:
        print(f'Something wen\'t wrong while loading {cogpath}\nError: {ex}\n\n')

############################################################################################################################################################

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    guild = bot.get_guild(int(data()['guild']))
    print("Serving Guild:")
    print(guild)
    changeStatus.start()
    print('\n' + text()['bot_ready'])
    print(text()['name'] + f': {bot.user.name}#{bot.user.discriminator}')
    print(f'ID: {bot.user.id}\n')
    #channel = bot.get_channel(data()['channelhello'])
    #await channel.send("Enfin Reveiller :)")

############################################################################################################################################################

#Status
status = ["!help", "Bot de Skyren"]

@tasks.loop(seconds = 5)
async def changeStatus():
    game = discord.Game(random.choice(status))
    await bot.change_presence(status = discord.Status.dnd, activity = game)

############################################################################################################################################################

#@slash.slash(description="invite me!")
#definingasync def invite(ctx):
  #await ctx.send("https://discord.com/api/oauth2/authorize?client_id=934479166307463239&permissions=8&scope=bot%20applications.commands")

@slash.slash(description="Shows New Fortnite Cosmetics")
async def new(ctx):
  await ctx.defer()
  url = "https://fortniteapi.io/v2/items/upcoming?lang=fr"
  headers = {
      "Authorization": fortnite_api_io_key
  }
  r = requests.get(url, headers=headers)
  print(r)
  data = r.json()
  embed=discord.Embed(title="Upcoming Fortnite Cosmetics", color=color)
  items = data['items']

  for item in items:
    embed.add_field(name=item['name'], value=f"**ID:** {item['id']}\n**Rarity:** {item['rarity']['name']}")
  embed.set_footer(text=footertext)
  await ctx.send(embed=embed)
    

@slash.slash(description="battle royale news")
async def brnews(ctx):
 
    response = requests.get(f'https://fortnite-api.com/v2/news/br?language=fr')

    geted = response.json()
        
    if response.status_code == 200:

        image = geted['data']['image']

        embed = discord.Embed(color=color)
        embed.set_image(url=image)
        embed.set_footer(text=footertext)

        await ctx.send(embed=embed)

    elif response.status_code == 400:
 
        error = geted['error']

        embed = discord.Embed(title='Error', 
                description=f'`{error}`')

        await ctx.send(embed=embed)

    elif response.status_code == 404:

        error =geted['error']

        embed = discord.Embed(title='Error', 
        description=f'``{error}``')

        await ctx.send(embed=embed)

@slash.slash(description="Creative Map Info")
async def island(ctx, code):
  await ctx.defer()
  url = f"https://fortniteapi.io/v1/creative/island?code={code}"
  headers = {
      "Authorization": fortnite_api_io_key
  }
  r = requests.post(url, headers=headers)
  data = r.json()
  embed=discord.Embed(title=data['island']['title'], description=f"Creator - {data['island']['creator']}", color=color)
  embed.add_field(name="Island Type", value=data['island']['islandPlotTemplate']['name'])
  embed.add_field(name="Published Date", value=data['island']['publishedDate'])
  embed.add_field(name="Description", value=data['island']['description'])
  embed.set_image(url=data['island']['image'])
  embed.set_footer(text=f"Tags - {data['island']['tags']}")
  embed.set_footer(text=footertext)
  await ctx.send(embed=embed)


@slash.slash(description="Get A Weapons WID")
async def wid(ctx, *, weapon):
    await ctx.defer()

    embed=discord.Embed(title=f"All Weapons Matching: {weapon}", color=color)
    url = "https://fortniteapi.io/v1/loot/list?lang=fr"
    headers = {
        "Authorization": fortnite_api_io_key
    }
    r = requests.post(url, headers=headers)
    data = r.json()
    wids = data['weapons']
    for item in wids:
      namee = item['name']
      if weapon.title() in namee:
        if item['rarity'] == "common":
          rarity = f"common | {bs}"
        if item['rarity'] == "uncommon":
          rarity = f"uncommon | {bs}{bs}"
        if item['rarity'] == "rare":
          rarity = f"rare | {bs}{bs}{bs}"
        if item['rarity'] == "epic":
          rarity = f"epic | {bs}{bs}{bs}{bs}"
        if item['rarity'] == "legendary":
          rarity = f"legendary | {bs}{bs}{bs}{bs}{bs}"
        if item['rarity'] == "mythic":
          rarity = f"mythic | {bs}{bs}{bs}{bs}{bs}{bs}"
        if item['rarity'] == "exotic":
          rarity = f"exotic | {bs}{bs}{bs}{bs}{bs}"
        embed.add_field(name=f"{namee} | {item['id']}", value=f"Rarity - **{rarity}**\n\n", inline=False)
    embed.set_footer(text=footertext)
    await ctx.send(embed=embed)


def source(o):
    s = inspect.getsource(o).split("\n")
    indent = len(s[0]) - len(s[0].lstrip())
    return "\n".join(i[indent:] for i in s)

def ready():
  source_ = source(discord.gateway.DiscordWebSocket.identify)
  patched = re.sub(
      r'([\'"]\$browser[\'"]:\s?[\'"]).+([\'"])',
      r"\1Discord Android\2",
      source_
  )

  loc = {}
  exec(compile(ast.parse(patched), "<string>", "exec"), discord.gateway.__dict__, loc)

  discord.gateway.DiscordWebSocket.identify = loc["identify"]

############################################################################################################################################################

@bot.command()
async def help(ctx):
  embed = discord.Embed(title= "__Command List__",
  description= "**Toutes les commands des membres/All member commands**",
  color= 0xFA0000)
  embed.add_field(name= "!porn + lettre", value= "envoie un gif porno", inline= False)
  embed.add_field(name= "!avatar + user", value= "envoie la photo de profil de la personne", inline= False)
  embed.add_field(name= "__**Fortnite**__", value= "**Commands Fortnite**", inline= False)
  embed.add_field(name= "!newcosmetics", value= "envoie les new cosmetics en format Json ou Embed", inline= False)
  embed.add_field(name= "!item + nom du cosmetics", value= "envoie un embed avec les infos du cosmetic", inline= False)
  embed.add_field(name= "!cc + nom du créateur", value= "envoie les infos du code créteur de la personne", inline= False)
  embed.add_field(name= "!aes", value= "envoie les cles des fichiers recent", inline= False)
  await ctx.send(embed=embed)

############################################################################################################################################################

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("Oups vous ne pouvez pas utilisez cette commande.")
    if isinstance(error, discord.Forbidden):
        await ctx.send("Oups, je n'ai pas les permissions nécéssaires pour faire cette commmande")
    else:
        raise error
try:
    bot.run(data()['Token'])
except Exception as e:
    print(e)
    exit()
