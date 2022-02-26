import discord
from discord.ext import commands 
import os
import random
from PIL import Image

#gif = Image.open(f"{os.path.dirname(os.path.abspath(__file__))}\\Commands\\Gif\\.gif")

############################################################################################################################################################

class membres(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    @commands.command(aliases=['profilepic','pfp'])
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title= f"{member}",color=0x40cc88, timestamp=ctx.message.created_at)
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)

############################################################################################################################################################

    @commands.command()
    async def poke(self, ctx):
        embed = discord.Embed(tilte= "Pokémon",
        description= "Vous avez capturez un pokémon")
        embed.set_image(url= random.choice())
        await ctx.send(embed=embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(membres(bot))