import nextcord
from nextcord.ext import commands

class mybot2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Events is loaded")
    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        await self.bot.get_channel(1054704591033335838).send(f"{member.mention} has joined the server")
    
def setup(bot):
    bot.add_cog(mybot2(bot))