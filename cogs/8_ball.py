import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import random


class mybot1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("8ball loaded")

    @nextcord.slash_command(
        name="hello",
        description="Say hello to the bot!",
    )
    async def hello(self, ctx: Interaction):
        await ctx.response.send_message(f"Hello, {ctx.user.mention}!")

    @nextcord.slash_command(name="8ball",description="gives you an random answer")
    async def Eightball(self, interaction : Interaction , question : str):
        response= ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",

                "Reply hazy, try again.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        embed=nextcord.Embed(title=":8ball:**8ball**", description=f":white_small_square: **Question:** {question}\n:white_small_square:**Answer: **{random.choice(response)}",color=nextcord.Color.random())
        embed.set_thumbnail(url="https://media.tenor.com/USELDeKObkgAAAAi/8ball-activity.gif")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(mybot1(bot))