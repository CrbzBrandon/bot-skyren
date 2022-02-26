import discord
from discord.ext import commands, tasks
from datetime import date, datetime
from Fortnite.Shop.concat_images import create_image_store

############################################################################################################################################################

class shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
############################################################################################################################################################

    @commands.command()
    async def shop(self, ctx):
        await create_image_store()
        day = datetime.now()
        month = day.strftime("%B")

        day = day.strftime("%A")

        if day == "Monday":
            day = "Lundi"
        elif day == "Tuesday":
            day = "Mardi"
        elif day == "Wednesday":
            day = "Mercredi"
        elif day == "Thursday":
            day = "Jeudi"
        elif day == "Friday":
            day = "Vendredi"
        elif day == "Saturday":
            day = "Samedi"
        elif day == "Sunday":
            day = "Dimanche"

        if month == "January":
            month = "Janvier"
        elif month == "February":
            month = "Fevrier"
        elif month == "March":
            month = "Mars"
        elif month == "April":
            month = "Avril"
        elif month == "May":
            month = "Mai"
        elif month == "June":
            month = "Juin"
        elif month == "July":
            month = "Juillet"
        elif month == "August":
            month = "Août"
        elif month == "September":
            month = "Septembre"
        elif month == "October":
            month = "Octobre"
        elif month == "November":
            month = "Novembre"
        elif month == "December":
            month = "Decembre"

        date_today = date.today()
        day_number = date_today.day
        year = date_today.year

        embed = discord.Embed(title= f"🛒 Boutique de Fortnite - du {day} {day_number} {month} {year}", colour=discord.Colour.blue())

        filee = discord.File("Fortnite/Shop/images/shop/shop.png")

        embed.description = "N'oubliez pas le code créateur Skyren dans la boutique"

        embed.set_image(url="attachment://shop.png")
  
        await ctx.send(file= filee, embed=embed)

############################################################################################################################################################

def setup(bot):
    bot.add_cog(shop(bot))