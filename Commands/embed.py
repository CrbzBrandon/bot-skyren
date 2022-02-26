import discord
from discord.ext import commands

############################################################################################################################################################

class embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    @commands.command()
    async def embed(self, ctx, member: discord.Member = None):
        embed = discord.Embed(
            title= "Google",
            description= "google.com",
            url= "https://www.google.com/", #Url du titre
            color= 0xc70000)
        embed.set_author(name= ctx.author.name, url= "https://www.google.com/", icon_url= "https://cdn.discordapp.com/attachments/812838848660504616/940299432103149658/images.png") #Url du nom
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/812838848660504616/940298909253791835/2048px-Google_22G22_Logo.png")
        embed.add_field(name= "name", value= "text", inline= True)
        embed.add_field(name= "name", value= "text", inline= True)
        embed.add_field(name= "name", value= "text", inline= False)
        embed.add_field(name= "name", value= "text", inline= False)
        embed.set_image(url= "https://cdn.discordapp.com/attachments/812838848660504616/940299016384704603/google-logo.png")
        embed.set_footer(text= f"{ctx.author}", icon_url= "")
        await ctx.send(embed=embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(embed(bot))