import json
import aiofiles
import aiohttp
import discord
from discord.ext import commands, tasks

############################################################################################################################################################

def parametre():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

############################################################################################################################################################

class aes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

############################################################################################################################################################

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            self.checkstatus.start()
        except Exception as ex:
            print(ex)
            self.checkstatus.stop()
            self.checkstatus.start()
        
############################################################################################################################################################

    @tasks.loop(seconds=15)
    async def checkstatus(self):
        await self.bot.wait_until_ready()
        try:
            Cached = json.loads(
                await (await aiofiles.open('Fortnite/Cache/aes.json', mode='r')).read())
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                    'https://benbot.app/api/v1/aes') as data:
                    if data.status != 200:
                        return
                    new = await data.json()
        except:
            return
        channel = self.bot.get_channel(938049213521076264)
        if new["mainKey"] != Cached["mainKey"]:
            await channel.send(embed=discord.Embed(color=0xfff000, title="Main AES Updated",
                                                   description=new["mainKey"]))
        if new["dynamicKeys"] != Cached["dynamicKeys"]:
            for i in new["dynamicKeys"]:
                if not i in Cached["dynamicKeys"]:
                    await channel.send(
                        embed=discord.Embed(color=0xfff000, title="New PAK encrypted",
                                            description="**" + str(i).split("/")[3] + "**\n" + new["dynamicKeys"][i]))
        await (await aiofiles.open('Fortnite/Cache/aes.json', mode='w+')).write(
            json.dumps(new, indent=2))

############################################################################################################################################################

    @commands.command()
    async def aes(self, ctx):
        await self.bot.wait_until_ready()
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(
                    'https://benbot.app/api/v1/aes') as data:
                    new = await data.json()
        except Exception as ex:
            print(ex)
            new = json.loads(
                await (await aiofiles.open('Fortnite/Cache/aes.json', mode='r')).read())
        embed = discord.Embed(color=0xfff000)
        embed.add_field(name=f"Build ID", value=new["version"], inline=False)
        embed.add_field(name=f"Main Key", value=new["mainKey"], inline=False)
        embed.add_field(name=f"Encrypted Paks", value="\u200B")
        string = "\u200B"
        count = 0
        for i in new["dynamicKeys"]:
            count += 1
            name = i
            key = new["dynamicKeys"][i]
            string += "**PAK-Name:**\n" + str(name) + "\n"
            string += "**PAK-Key:**\n" + str(key) + "\n"
            string += "\n"
            if count >= 3:
                embed.add_field(name=f"\u200B", value=f"{string}", inline=False)
                await ctx.send(embed=embed)
                string = "\u200B"
                count = 0
                embed = discord.Embed(color=0xfff000)
        embed.add_field(name=f"\u200B", value=f"{string}", inline=False)
        await ctx.send(embed=embed)

############################################################################################################################################################

    def cog_unload(self):
        self.checkstatus.stop()
        try:
            self.client.unload_extension("cogs.aes")
        except:
            pass
        try:
            self.client.load_extension("cogs.aes")
        except:
            pass

############################################################################################################################################################

def setup(bot):
    bot.add_cog(aes(bot))
