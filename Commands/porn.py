import discord
from discord.ext import commands
import random

############################################################################################################################################################

from Commands.Porns.anal import *
from Commands.Porns.black import *
from Commands.Porns.gay import *
from Commands.Porns.hentai import *
from Commands.Porns.lesbienne import *
from Commands.Porns.milf import *
from Commands.Porns.teen import *
from Commands.Porns.trans import *

############################################################################################################################################################

#https://www.pornologie.fr/category/top/gif/

phrase = ["Tu aimes sa", "Sa te fait bander", "Petit coquin :)"]

############################################################################################################################################################

class porn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    @commands.command()
    async def porn(self, ctx, *parametre):
        parametre = " ".join(parametre)

        if parametre == "":
            embed = discord.Embed(title= "__Commands Porn__",
            description= "Liste des Porn GIF",
            color= 0xc70000)
            embed.add_field(name= "__Porn__", value= "`a` => Porn Anal\n`b` => Porn Black\n`g` => Porn Gay\n`l` => Porn Lesbienne\n`m` => Porn Milf\n`te` => Porn Teen (Pas cor disponible)\n`tr` => Porn Trans (Pas cor disponible)", inline= False)
            embed.add_field(name= "__Hentai__", value= "`h` => Porn Hentai", inline= False)
            await ctx.send(embed=embed)

        elif parametre == "a":
            embed = discord.Embed(title= "__Porn Anal__")
            embed.set_image(url=random.choice(pornanal))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)
        
        elif parametre == "b":
            embed = discord.Embed(title= "__Porn Black__")
            embed.set_image(url=random.choice(pornblack))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

        elif parametre == "g":
            embed = discord.Embed(title= "__Porn Gay__")
            embed.set_image(url=random.choice(porngay))
            embed.set_footer(text= f"{ctx.author} 🫃 tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

        elif parametre == "h":
            embed = discord.Embed(title= "__Porn Hentai__")
            embed.set_image(url=random.choice(pornhentai))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

        elif parametre == "l":
            embed = discord.Embed(title= "__Porn Lesbienne__")
            embed.set_image(url=random.choice(pornlesbienne))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

        elif parametre == "m":
            embed = discord.Embed(title= "__Porn Milf__")
            embed.set_image(url=random.choice(pornmilf))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

        elif parametre == "te":
            embed = discord.Embed(title= "__Porn Teen__")
            embed.set_image(url=random.choice(pornteen))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

        elif parametre == "tr":
            embed = discord.Embed(title= "__Porn Trans__")
            embed.set_image(url=random.choice(porntrans))
            embed.set_footer(text= f"{ctx.author} tu kiff sa ?/do you like it ?")
            await ctx.send(embed=embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(porn(bot))