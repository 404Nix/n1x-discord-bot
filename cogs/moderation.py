import nextcord, datetime
from nextcord import Interaction, SlashOption
from nextcord.ext import commands


class mybot4(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation is loaded")

    @nextcord.slash_command(name="ping")
    async def ping(self, ctx:Interaction):
        em = nextcord.Embed()
        em.add_field(name="Ping", value=f"pong! `{round(self.bot.latency * 1000)}`ms", inline=True)
        await ctx.send(embed=em)
        
    @nextcord.slash_command(name="kick")
    async def kick(self, ctx : Interaction, member : nextcord.Member, reason : str = SlashOption(required=False)):
        if not reason : reason = "No reason provided"
        #await member.kick(reason=reason)
        dm = nextcord.Embed(description=f'```WARNING \nYou have been kicked from {member.guild.name}\nDM Admin to add you again ```')
        await member.send(embed=dm)
        await ctx.response.send_message(f"Name: {member.name}\nID: {member.id}\nreason: {reason}\nkicked")

        
        
def setup(bot):
    bot.add_cog(mybot4(bot))
















# class test(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.Cog.listener()
#     async def on_ready(self):
#         print("ready to go")

#     @commands.command()
#     async def ping(self, ctx):
#         await ctx.send("pong!")


# def setup(bot):
#     bot.add_cog(test(bot))