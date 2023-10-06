import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Interaction, SlashOption
import requests
import aiohttp, asyncio

class mybot3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("nsfw is loaded")

    @nextcord.slash_command(name="nsfw-one", description="multiple nsfw commands in one go!")
    @application_checks.is_nsfw()
    async def nsfw(self, ctx:Interaction, commands: 
                   str = SlashOption(choices=['genshin', 'swimsuit', 'schoolswimsuit', 'white',
                                               'barefoot', 'touhou', 'gamecg', 'hololive', 'uncensored',
                                                 'sunglasses', 'glasses', 'weapon', 'shirtlift', 
                                                 'chain', 'fingering', 'flatchest', 'torncloth', 
                                                 'bondage', 'demon', 'wet', 'pantypull', 'headdress', 
                                                 'headphone', 'tie', 'anusview'], required=True)):
            

            async with aiohttp.ClientSession() as session:
                 await ctx.response.defer()
                 async with session.get(f'https://fantox-apis.vercel.app/{commands}') as r:
                        if r.status == 200:
                           js = await r.json()
                           nsfw = nextcord.Embed(title=commands, color=nextcord.Color.dark_red())
                           nsfw.set_image(url=js['url'])
                           await ctx.followup.send(embed=nsfw)
                        else:
                             await ctx.response.send_message("error occured!")

    @nsfw.error
    async def nsfw_error(self, ctx, error):
        if isinstance(error, application_checks.ApplicationNSFWChannelRequired):
            embed=nextcord.Embed(description=f"```NSFW⚠️!! You can not run this command here\n{error}```")
            await ctx.send(embed=embed)
        else:
            embed=nextcord.Embed(description=f"```Something went wrong. Please try again..!!\n{error}```")
            await ctx.send(embed=embed)


    
    @nextcord.slash_command(name="nsfw-two", description="multiple nsfw commands in one go!")
    @application_checks.is_nsfw()
    async def nsfw2(self, ctx:Interaction, commands: 
                   str = SlashOption(choices=['shorts','stokings', 'topless', 'beach', 
                                              'bunnygirl', 'bunnyear', 'idol', 'vampire',
                                                'gun', 'maid', 'bra', 'nobra', 'bikini', 
                                                'whitehair', 'blonde', 'pinkhair', 'bed', 
                                                'ponytail', 'nude', 'dress', 'underwear',
                                                  'foxgirl', 'uniform', 'skirt'], required=True)):
            

            async with aiohttp.ClientSession() as session:
                 await ctx.response.defer()
                 async with session.get(f'https://fantox-apis.vercel.app/{commands}') as r:
                        if r.status == 200:
                           js = await r.json()
                           nsfw = nextcord.Embed(title=commands, color=nextcord.Color.dark_red())
                           nsfw.set_image(url=js['url'])
                           await ctx.followup.send(embed=nsfw)
                        else:
                             await ctx.response.send_message("error occured!")

    @nsfw2.error
    async def nsfw2_error(self, ctx, error):
        if isinstance(error, application_checks.ApplicationNSFWChannelRequired):
            embed=nextcord.Embed(description=f"```NSFW⚠️!! You can not run this command here\n{error}```")
            await ctx.send(embed=embed)
        else:
            embed=nextcord.Embed(description=f"```Something went wrong. Please try again..!!\n{error}```")
            await ctx.send(embed=embed)



    @nextcord.slash_command(name="nsfw-three", description="multiple nsfw commands in one go!")
    @application_checks.is_nsfw()
    async def nsfw3(self, ctx:Interaction, commands: 
                   str = SlashOption(choices=['sex', 'sex2', 'sex3', 'breast', 
                                              'twintail', 'spreadpussy', 'tears', 'seethrough', 
                                                  'breasthold', 'drunk', 'fateseries', 
                                                  'spreadlegs', 'openshirt', 'headband', 
                                                  'food', 'close', 'tree', 'nipples', 
                                                  'erectnipples', 'horns', 'greenhair',
                                                    'wolfgirl', 'catgirl'], required=True)):
            

            async with aiohttp.ClientSession() as session:
                 await ctx.response.defer()
                 async with session.get(f'https://fantox-apis.vercel.app/{commands}') as r:
                        if r.status == 200:
                           js = await r.json()
                           nsfw = nextcord.Embed(title=commands, color=nextcord.Color.dark_red())
                           nsfw.set_image(url=js['url'])
                           await ctx.followup.send(embed=nsfw)
                        else:
                             await ctx.response.send_message("error occured!")

    @nsfw3.error
    async def nsfw3_error(self, ctx, error):
        if isinstance(error, application_checks.ApplicationNSFWChannelRequired):
            embed=nextcord.Embed(description=f"```NSFW⚠️!! You can not run this command here\n{error}```")
            await ctx.send(embed=embed)
        else:
            embed=nextcord.Embed(description=f"```Something went wrong. Please try again..!!\n{error}```")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(mybot3(bot))