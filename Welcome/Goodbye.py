from functools import total_ordering
import discord
from discord.ext import commands
from PIL import Image, ImageOps, ImageDraw, ImageFont
import requests
from io import BytesIO
import os

############################################################################################################################################################

#Config
channel_id = 938916926523060306
guild_id = 863187121665998869

############################################################################################################################################################

headerMessage = "Aurevoir !\nGoodbye !"
headerFont = "Takoyaki.ttf"
userFont = "Takoyaki.ttf"
memberFont = "Takoyaki.ttf"

#Text outline
def outline(draw,x,y,text,font):
    draw.text((x-2, y), text, font=font, fill="Black") #couleur du contour du texte image
    draw.text((x+2, y), text, font=font, fill="Black")
    draw.text((x, y-2), text, font=font, fill="Black")
    draw.text((x, y+2), text, font=font, fill="Black")

#Make welcome banner
def bannerMake(avUrl,userName, userCount):
    #get profile picture
    url = avUrl
    name = userName.upper()
    response = requests.get(url)
    pfpImg = Image.open(BytesIO(response.content))
    pfpImg = pfpImg.resize((200, 200)) #largeur et hauteur de la photo de profil
    outlinesize= (210,210) #largeur et hauteur du contour de la photo de profil
    #crop circular pfp
    bigsize = (pfpImg.size[0] * 3, pfpImg.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    pfpmask = mask.resize(pfpImg.size, Image.ANTIALIAS)
    outlinemask = mask.resize(outlinesize, Image.ANTIALIAS)
    pfpImg.putalpha(pfpmask)

    pfpoutline = Image.new('RGBA',outlinesize,(246,16,81,1)) #couleur de cercle
    pfpoutline.putalpha(outlinemask)
    #add pfp to background
    background = Image.open('Welcome/banner1.png')
    x,y = (750,60) #emplacement de la photo de profil
    background.paste(pfpoutline,(x-5,y-5),pfpoutline) #emplacement du cercle par rapport a la photo de profil
    background.paste(pfpImg,(x, y), pfpImg)
    
    #Text
    W, H = (background.width,background.height)
    draw = ImageDraw.Draw(background)

    #Header
    header = headerMessage
    font = ImageFont.truetype('Welcome/Fonts/%s'%headerFont, 75) #taille de l'écriture
    x, y = (330,90) #emplacement de l'écriture
    outline(draw,x,y,header,font)
    draw.text((x, y), header, font=font, fill= "#5894D0")

    #Discord Name
    font = ImageFont.truetype('Welcome/Fonts/%s'%userFont, 50)
    x, y = (420,280)
    outline(draw,x,y,name,font)
    draw.text((x, y), name, font=font, fill= "#5894D0")

    #Member count
    message = "Bonne continuation !\nGood continuation !"
    font = ImageFont.truetype('Welcome/Fonts/%s'%memberFont, 50)
    x, y = (420,340)
    outline(draw,x,y,message,font)
    draw.text((x, y), message, font=font, fill= "#5894D0")

    #background.show()
    #banner output
    if os.path.exists('Welcome/output1.png'):
        os.remove('Welcome/output1.png')
        background.save('Welcome/output1.png')
    else:
        background.save('Welcome/output1.png')

############################################################################################################################################################

class Goodbye(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Goodbye Ready!")
    
############################################################################################################################################################

    #Member Leave event
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.bot.wait_until_ready()
        url = member.avatar_url
        name = member.name
        guild = self.bot.get_guild(int(guild_id))
        total_members = guild.member_count
        print("User %s Left"%name)
        try:
            bannerMake(url,name,total_members)
        except:
            print("Banner Make Error")
        channel = self.bot.get_channel(int(channel_id))
        try:
            message = await channel.send(content="%s à quitté le serveur ! / leave the server !"%member.name,file=discord.File('Welcome/output1.png'))
        except:
            print("Banner Send Error")

############################################################################################################################################################

def setup(bot):
    bot.add_cog(Goodbye(bot))