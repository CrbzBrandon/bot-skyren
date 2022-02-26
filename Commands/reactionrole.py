import discord
from discord.ext import commands 
from discord.utils import get

############################################################################################################################################################

#Emoji Config \:emoji: sur discord
Idmessage = 941051346088505427
emoji1 = "🇫🇷"
emoji2 = "🇬🇧"

############################################################################################################################################################

class ReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#    @commands.Cog.listener()
#    async def on_ready(self):
#        print("ReactionRole Ready!")

############################################################################################################################################################

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        ourMessageID = Idmessage 
        
        if ourMessageID == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == emoji1:
                role = discord.utils.get(guild.roles, name= "français")#Nom du rôle
            elif emoji == emoji2:
                role = discord.utils.get(guild.roles, name= "english")#Nom du rôle
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        ourMessageID = Idmessage

        if ourMessageID == payload.message_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == emoji1:
                role = discord.utils.get(guild.roles, name= "français")#Nom du rôle
            elif emoji == emoji2:
                role = discord.utils.get(guild.roles, name= "english")#Nom du rôle
            member = await(guild.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member not found")

############################################################################################################################################################

    #Réaction Rôle Embed
    @commands.command()
    async def role(self, ctx):
        embed = discord.Embed(
            title= "__Actus Fortnite__",
            description= "Votre Language/Your Language"      
        )
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(emoji1)#Fr
        await msg.add_reaction(emoji2)#En

############################################################################################################################################################

def setup(bot):
    bot.add_cog(ReactionRole(bot))