import nextcord
from nextcord import Interaction,SlashOption
from nextcord.ext import commands
import aiohttp, datetime

class neko(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("neko loaded🐱")
        
    @nextcord.slash_command(name="neko", description="All types of neko commands using neko API")
    async def neko(self, interaction:Interaction, commands : str = SlashOption(name="type",
        description="All types of neko commands using neko API", choices=['husbando','neko','waifu','baka',
                                                                          'bite','cry','blush',
                                                                          'cuddle', 'dance','feed',
                                                                          'happy','hug', 'kick',
                                                                          'kiss', 'laugh', 'nope', 'pat',
                                                                          'poke', 'pout', 'punch', 'shoot',
                                                                           'slap', 'sleep', 'smile',
                                                                          'wink'])):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://nekos.best/api/v2/{commands}") as r:
                if r.status == 200:
                    js = await r.json()
                    embed = nextcord.Embed(color=nextcord.Color.dark_magenta(),timestamp=datetime.datetime.now())
                    #embed.set_author(name=f"{js['results'][0]['artist_name']}", url=f"{js['results'][0]['source_url']}")
                    embed.set_image(url=f"{js['results'][0]['url']}")
                    #embed.set_footer(text=f"Created by {js['results'][0]['artist_name']}", icon_url=f"{interaction.user.avatar}")
                    await interaction.response.send_message(embed=embed)
                else:
                    embed = nextcord.Embed(description="```**Error occured while requesting data from API**```")
                    
def setup(bot):
    bot.add_cog(neko(bot))