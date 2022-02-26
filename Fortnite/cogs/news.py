import json
from datetime import datetime
import requests
import discord
from discord.ext import commands, tasks

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


response_lang = 'en' if data()['Response lang'] == '' else data()['Response lang']
request_lang = 'en' if data()['Search lang'] == '' else data()['Search lang']

############################################################################################################################################################

class news(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    @tasks.loop(seconds=60)
    async def brnews(self, l = None):
        res_lang = response_lang
        if l == None:
            res_lang = response_lang
        response = requests.get(f'https://fortnite-api.com/v2/news/br?language={res_lang}')
        geted = response.json()
        channel = self.bot.get_channel(data()['channelnews'])

        if response.status_code == 200:
            image = geted['data']['image']
            embed = discord.Embed(title=text()['br_news'])
            embed.set_image(url=image)
            await channel.send(embed=embed)

        elif response.status_code == 400: 
            error = geted['error']
            embed = discord.Embed(title='Error', 
                description=f'`{error}`')
            await channel.send(embed=embed)

        elif response.status_code == 404:
            error =geted['error']
            embed = discord.Embed(title='Error', 
            description=f'``{error}``')
            await channel.send(embed=embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(news(bot))
