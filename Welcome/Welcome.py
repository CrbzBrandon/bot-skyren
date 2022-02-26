import discord
from discord.ext import commands
from PIL import Image, ImageOps, ImageDraw, ImageFont
import requests
from io import BytesIO
import os

############################################################################################################################################################

#Config
channel_id = 863187122176131096
guild_id = 863187121665998869
role_id = 863193319693090836

############################################################################################################################################################

headerMessage = "Bienvenue !/Welcome !"
headerFont = "Takoyaki.ttf"
userFont = "Takoyaki.ttf"
memberFont = "Takoyaki.ttf"

#Text outline
def outline(draw,x,y,text,font):
    draw.text((x-1, y), text, font=font, fill="Black") #couleur du contour du texte image
    draw.text((x+1, y), text, font=font, fill="Black")
    draw.text((x, y-1), text, font=font, fill="Black")
    draw.text((x, y+1), text, font=font, fill="Black")

#Make welcome banner
def bannerMake(avUrl,userName, userCount):
    #get profile picture
    url = avUrl
    name = userName.upper()
    memberCount = str(userCount)
    print(name+ " : "+memberCount)
    response = requests.get(url)
    pfpImg = Image.open(BytesIO(response.content))
    pfpImg = pfpImg.resize((200, 200))
    outlinesize= (204,205)
    #crop circular pfp
    bigsize = (pfpImg.size[0] * 3, pfpImg.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    pfpmask = mask.resize(pfpImg.size, Image.ANTIALIAS)
    outlinemask = mask.resize(outlinesize, Image.ANTIALIAS)
    pfpImg.putalpha(pfpmask)

    pfpoutline = Image.new('RGBA',outlinesize,(255,255,255,255))
    pfpoutline.putalpha(outlinemask)
    #add pfp to background
    background = Image.open('Welcome/banner.png')
    x,y = (210,60)
    background.paste(pfpoutline,(x-2,y-2),pfpoutline)
    background.paste(pfpImg,(x, y), pfpImg)
    #Text

    W, H = (background.width,background.height)
    draw = ImageDraw.Draw(background)

    #Header
    header = headerMessage
    font = ImageFont.truetype('Welcome/Fonts/%s'%headerFont, 70)
    x, y = (60,280)
    outline(draw,x,y,header,font)
    draw.text((x, y), header, font=font, fill= "#98251B")

    #Discord Name
    font = ImageFont.truetype('Welcome/Fonts/%s'%userFont, 50)
    x, y = (60,350)
    outline(draw,x,y,name,font)
    draw.text((x, y), name, font=font, fill= "#98251B")

    #Member count
    message = "Tu es le/You are the %s eme membres/th member"%memberCount
    font = ImageFont.truetype('Welcome/Fonts/%s'%memberFont, 35)
    x, y = (60,410)
    outline(draw,x,y,message,font)
    draw.text((x, y), message, font=font, fill= "#98251B")

    #background.show()
    #banner output
    if os.path.exists('Welcome/output.png'):
        os.remove('Welcome/output.png')
        background.save('Welcome/output.png')
    else:
        background.save('Welcome/output.png')

############################################################################################################################################################

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Welcome Ready!")
    
############################################################################################################################################################

    #Member Join event
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.bot.wait_until_ready()
        url = member.avatar_url
        name = member.name + "#" + member.discriminator
        guild = self.bot.get_guild(int(guild_id))
        total_members = guild.member_count
        print("User %s Joined"%name)
        #roles = guild.get_role(role_id)
        #await member.add_roles(roles)
        try:
            bannerMake(url,name,total_members)
        except:
            print("Banner Make Error")
        channel = self.bot.get_channel(int(channel_id))
        try:
            message = await channel.send(content="Bienvenue sur Skyren Fn ! / Welcome on Skyren Fn !",file=discord.File('Welcome/output.png'))
        except:
            print("Banner Send Error")


############################################################################################################################################################

    #Member Leave event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.wait_until_ready()
        name = member.name
        print("User %s Left"%name)
        guild = self.bot.get_guild(int(guild_id))
        total_members = guild.member_count

############################################################################################################################################################

def setup(bot):
    bot.add_cog(Welcome(bot))