import time
import discord
from discord.ext import commands

############################################################################################################################################################

MOD_ROLE = 863191160892686388
LOCK_CATEGORIES = [938052052519641149]

############################################################################################################################################################

class lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
############################################################################################################################################################

    async def get_lock_categories(self, guild, categories):
        lock_categories = []
        if len(categories) != 0:
            for category in categories:
                lock_categories.append(guild.get_channel(category))
            return lock_categories
        else:
            print("Please configure the locked categories at the top of lock.py")

    async def status_embed(self, ctx, description):
        guild = ctx.author.guild
        everyone_role = discord.utils.get(guild.roles, name="member")
        channelarr = ctx.author.guild.channels
        embed = discord.Embed()
        embed.set_author(name=description)
        for category in ctx.author.guild.by_category():
            value = ""
            for channel in category[1]:
                if isinstance(channel, discord.TextChannel):
                    send = channel.overwrites_for(everyone_role).send_messages
                    if send:
                        emoji = "\u2705"
                    elif send == False:
                        emoji = "\U0001F512"
                    else:
                        emoji = "\u3030"
                    value += f"{channel.mention}\t\t{emoji}\n"
            embed.add_field(name=category[0], value=value, inline=False)
        return embed

    async def channel_lock(self, everyone, channel):
        await channel.set_permissions(everyone, send_messages=False, reason="Automatic channel locking")

    async def channel_unlock(self, everyone, channel):
        await channel.set_permissions(everyone, send_messages=True, reason="Automatic channel unlocking")

############################################################################################################################################################

    @commands.command()
    @commands.has_role(MOD_ROLE)
    async def lock(self, ctx, *args):
        """------ channels by \'all\' if configured, or by a list of channels"""
        guild = ctx.author.guild
        everyone_role = discord.utils.get(guild.roles, name="member")
        if len(args) == 1 and "all" in args:
            # Lock all from LOCK_CATEGORIES
            lock_categories = await self.get_lock_categories(guild, LOCK_CATEGORIES)
            lock_string = ', '.join(map(str, lock_categories))
            embed = discord.Embed(description=f"Locking channels in {lock_string}...")
            message = await ctx.send(embed=embed)
            for category in ctx.author.guild.by_category():
                if category[0] in lock_categories:
                    for channel in category[1]:
                        await self.channel_lock(everyone_role, channel)
            time.sleep(2)
            embed = await self.status_embed(ctx, description=f"Locked channels in category \'{lock_string}\'")
            await message.edit(embed = embed)
        else:
            lock_array = []
            for arg in args:
                channel = discord.utils.find(lambda m: m.mention == arg or m.name == arg, guild.text_channels)
                if channel == None:
                    await ctx.send(f"Channel `{arg}` not found. Please try again.")
                else:
                    await self.channel_lock(everyone_role, channel)
                    lock_array.append(channel)
            embed = await self.status_embed(ctx, description=f"Locked channels {', '.join(map(str, lock_array))}")
            await ctx.send(embed = embed)

############################################################################################################################################################
        
    @commands.command()
    @commands.has_role(MOD_ROLE)
    async def unlock(self, ctx, *args):
        guild = ctx.author.guild
        """------ unlocks channels by \'all\' if configured, or by a list of channels"""
        guild = ctx.author.guild
        everyone_role = discord.utils.get(guild.roles, name="member")
        if len(args) == 1 and "all" in args:
            lock_categories = await self.get_lock_categories(guild, LOCK_CATEGORIES)
            everyone_role = discord.utils.get(guild.roles, name="member")
            lock_string = ', '.join(map(str, lock_categories))
            embed = discord.Embed(description=f"Unlocking channels in {lock_string}...")
            message = await ctx.send(embed=embed)
            for category in ctx.author.guild.by_category():
                if category[0] in lock_categories:
                    for channel in category[1]:
                        await self.channel_unlock(everyone_role, channel)
            time.sleep(2)
            embed = await self.status_embed(ctx, description=f"Unlocked channels in category \'{lock_string}\'")
            await message.edit(embed = embed)
        else:
            lock_array = []
            for arg in args:
                channel = discord.utils.find(lambda m: m.mention == arg or m.name == arg, guild.text_channels)
                if channel == None:
                    await ctx.send(f"Channel `{arg}` not found. Please try again.")
                else:
                    await self.channel_unlock(everyone_role, channel)
                    lock_array.append(channel)
            embed = await self.status_embed(ctx, description=f"Unlocked channels {', '.join(map(str, lock_array))}")
            await ctx.send(embed = embed)

############################################################################################################################################################

    @commands.command()
    @commands.has_role(MOD_ROLE)
    async def status(self, ctx):
        """------ checks the status for all channels"""
        embed = await self.status_embed(ctx, description="Send Message permissions for member")
        message = await ctx.send(embed=embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(lock(bot))