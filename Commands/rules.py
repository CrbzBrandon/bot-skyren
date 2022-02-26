import discord
from discord.ext import commands
from discord.utils import get

############################################################################################################################################################

guild_id = 863187121665998869 #id du serveur
rolemodo = 863191515152384000 #id du role modo
roleadmin = 863191160892686388 #id du role admin
channelpub = 938053777481687055 #id du channel pub
channelen = 938472671111442522 #id du chat englais
channelfr = 938052145851293716 #id du chat francais
idmessagefr = 939215901721513984
idmessageen = 939216296665546762
MOD_ROLE = 863191160892686388 

############################################################################################################################################################

class rules(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        ourMessageID = idmessagefr
        
        if ourMessageID == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == "\u2705":
                role = discord.utils.get(guild.roles, name= "member")#Nom du rôle
            await member.add_roles(role)

        ourMessageID = idmessageen
        
        if ourMessageID == payload.message_id:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == "\u2705":
                role = discord.utils.get(guild.roles, name= "member")#Nom du rôle
            await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        ourMessageID = idmessagefr
        

        if ourMessageID == payload.message_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == "\u2705":
                role = discord.utils.get(guild.roles, name= "member")#Nom du rôle
            member = await(guild.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member not found")

        ourMessageID = idmessageen

        if ourMessageID == payload.message_id:
            guild = await(self.bot.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            if emoji == "\u2705":
                role = discord.utils.get(guild.roles, name= "member")#Nom du rôle
            member = await(guild.fetch_member(payload.user_id))
            if member is not None:
                await member.remove_roles(role)
            else:
                print("Member not found")

############################################################################################################################################################

    @commands.command()
    @commands.has_role(MOD_ROLE)
    async def regles(self, ctx):
        embed = discord.Embed(color= 0xc70000)
        embed.set_image(url= "https://cdn.discordapp.com/attachments/938886670441386045/939195483124015104/FR_13BR_Discord_Banners_Server_Rules.jpg")
        message = await ctx.send(embed=embed),
        guild = ctx.bot.get_guild(int(guild_id))
        embed = discord.Embed(
            title= "__Réglement__",
            description= f"Voici les régles de {guild}",
            color= 0xc70000)
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/938886670441386045/939186073957974086/PicsArt_02-04-04.49.31.png")
        embed.add_field(name= "I – Comportement \n\u3030", value= "> -Restez courtois, poli. Vous pouvez être familier, nous ne vous demandons pas d’écrire comme Molière, nous ne sommes pas à L’Élysée \n\n> -Pas de violence verbale gratuite. Vous pouvez taquiner gentiment sans aller dans l’extrême. Si cela reste dans la bonne humeur et le second degré nous le tolérons. Si le staff ou moi même estimons que cela ne respecte plus la règle, vous risquez un kick ou un ban en fonction de l’humeur de la personne qui s'occupe de votre cas (en général c’est un ban direct avec moi) \n\u3030", inline= False)
        embed.add_field(name= "II – Chat écrit/ vocal \n\u3030", value= f"> -Pas de spam, sous peine de bannissement. \n\n> -Pas de pub sur les différents chats (sauf celui <#{channelpub}>), sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte \n\u3030", inline= False)
        embed.add_field(name= "III – Profil/Pseudo \n\u3030", value= "> -Ne doit pas être ressemblant/confondu avec celui d’un membre du staff, sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte. \n\n> -Ne doit pas contenir de propos racistes, homophobes, sexistes … (genre la photo de profil Hitler on s’en passera) sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte. \n\n> -Ne doit pas avoir de caractère pornographique, sous peine d’avertissement puis ban si l’avertissement n’est pas pris en compte. \n\u3030", inline= False)
        embed.add_field(name= "IV - Contacter le staff \n\u3030", value= f"> -Si pour une quelconque raison, vous voulez contacter un membre du staff (modo ou admin), mentionner <@&{rolemodo}> ou/et <@&{roleadmin}> sur le <#{channelfr}> \n\n> -Si vous voulez entrer dans l’équipe de modération, contactez les <@&{roleadmin}>. Afin de devenir <@&{rolemodo}> vous passerez un genre d’entretien afin de voir vos motivations et vos idées pour améliorer le serveur. Ne stressez pas non plus, si vous êtes légitime ça se passera bien <:angel:938732402698756096>. C’est histoire de voir à qui je donne le rôle de modo et d’apprendre à la connaître. La décision vous sera donnée ultérieurement par message privé. \n\n\n*Ces règles peuvent être soumises à des évolutions au cours du temps. Vous avez ici la base du règlement !!!*", inline= False)
        embed.set_image(url= "https://cdn.discordapp.com/attachments/938886670441386045/939196546120036382/inconnu.jpeg")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("\u2705")

############################################################################################################################################################

    @commands.command()
    @commands.has_role(MOD_ROLE)
    async def rules(self, ctx):
        embed = discord.Embed(color= 0xc70000)
        embed.set_image(url= "https://cdn.discordapp.com/attachments/938886670441386045/939200146758074488/EN_13BR_Discord_Banners_Server_Rules.jpg")
        message = await ctx.send(embed=embed),
        guild = ctx.bot.get_guild(int(guild_id))
        embed = discord.Embed(
            title= "__Rules__",
            description= f"Here are the rules of {guild}",
            color= 0xc70000)
        embed.set_thumbnail(url= "https://cdn.discordapp.com/attachments/938886670441386045/939186073957974086/PicsArt_02-04-04.49.31.png")
        embed.add_field(name= "I – Behavior \n\u3030", value= "> -Be courteous, polite. You can be familiar, we do not ask you to write like Molière, we are not at the Elysée Palace \n\n> -No gratuitous verbal abuse. You can tease nicely without going to extremes. If it remains in good humor and second degree we tolerate it. If the staff or me even estimate that that does not respect the rule any more, you risk a kick or a ban according to the mood of the person who deals with your case (in general it is a direct ban with me) \n\u3030", inline= False)
        embed.add_field(name= "II – Written/vocal chat \n\u3030", value= f"> -No spam, on pain of being banned. \n\n> -No ads on the different chats (except the <#{channelpub}> one), under penalty of warning then ban if the warning is not heeded \n\u3030", inline= False)
        embed.add_field(name= "III – Profile/Nickname \n\u3030", value= "> -Must not resemble/conflict with that of a staff member, under penalty of warning then ban if the warning is not heeded. \n\n> -Must not contain racist, homophobic, sexist remarks... (like the Hitler profile picture) under penalty of warning then ban if the warning is not taken into account. \Must not have pornographic character, under penalty of warning then ban if the warning is not taken into account. \n\u3030", inline= False)
        embed.add_field(name= "IV - Contact the staff \n\u3030", value= f"> -If for any reason, you want to contact a staff member (modo or admin), mention <@&{rolemodo}> or/and <@&{roleadmin}> on the <#{channelen}> \n\n> -If you want to join the moderation team, contact the <@&{roleadmin}>. In order to become <@&{rolemodo}> you will have to pass a kind of interview to see your motivations and your ideas to improve the server. Don't stress either, if you are legitimate it will go well <:angel:938732402698756096>. It's just to see who I give the role of modo to and to get to know her. The decision will be given to you later by private message. \n\n\n*These rules may be subject to change over time. You have here the basis of the rules!!!*", inline= False)
        embed.set_image(url= "https://cdn.discordapp.com/attachments/938886670441386045/939196546120036382/inconnu.jpeg")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("\u2705")

############################################################################################################################################################

def setup(bot):
    bot.add_cog(rules(bot))