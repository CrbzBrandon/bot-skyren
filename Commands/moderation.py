import discord
from discord.ext import commands

############################################################################################################################################################

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    #Commands Ban 
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user : discord.User, *reason):
        reason = " ".join(reason)
        await ctx.guild.ban(user, reason = reason)
        await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

############################################################################################################################################################

    #Commands Unban 
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, user, *reason):
        reason = " ".join(reason)
        userName, userId = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for i in bannedUsers:
            if i.user.name == userName and i.user.discriminator == userId:
                await ctx.guild.unban(i.user, reason = reason)
                await ctx.send(f"{user} à été unban.")
                return
        #Ici on sait que lutilisateur na pas ete trouvé
        await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

############################################################################################################################################################

    #Commands Kick 
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def kick(self, ctx, user : discord.User, *reason):
        reason = " ".join(reason)
        await ctx.guild.kick(user, reason = reason)
        await ctx.send(f"{user} à été kick.")

############################################################################################################################################################

    #Crée le rôle mute
    @commands.Cog.listener()
    async def createMutedRole(self, ctx):
        mutedRole = await ctx.guild.create_role(name = "Muted",
        permissions = discord.Permissions(send_messages = False,speak = False),reason = "Creation du role Muted pour mute des gens.")
        for channel in ctx.guild.channels:
            await channel.set_permissions(mutedRole, send_messages = False, speak = False)
        return mutedRole

    @commands.Cog.listener()
    async def getMutedRole(self, ctx):
        roles = ctx.guild.roles
        for role in roles:
            if role.name == "Muted":
                return role
    
        return await self.createMutedRole(ctx)

############################################################################################################################################################

    #Commands Mute
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def mute(self, ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
        mutedRole = await self.getMutedRole(ctx)
        await member.add_roles(mutedRole, reason = reason)
        await ctx.send(f"{member.mention} a été mute !")

############################################################################################################################################################
    
    #Commands Unmute
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unmute(self, ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
        mutedRole = await self.getMutedRole(ctx)
        await member.remove_roles(mutedRole, reason = reason)
        await ctx.send(f"{member.mention} a été unmute !")

############################################################################################################################################################

    #Commands Clear
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def clear(self, ctx, nombre : int):
        messages = await ctx.channel.history(limit = nombre + 1).flatten()
        for message in messages:
            await message.delete()

    #Commands ClearAll
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def clearall(self, ctx):
        messages = await ctx.channel.history().flatten()
        for message in messages:
            await message.delete()

############################################################################################################################################################

    @commands.command()
    async def test(self, ctx):
        messages = await ctx.channel.history(limit= 1).flatten()
        for message in messages:
            await message.delete()
        embed = discord.Embed(title= "Clear your command",
        description = "test")
        await ctx.send(embed = embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(moderation(bot))