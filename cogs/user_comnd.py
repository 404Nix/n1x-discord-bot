import nextcord
from nextcord.ext import commands

class mybot5(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("user_commands loaded")

    @nextcord.user_command()
    async def memberinfo(self, interaction: nextcord.Interaction, member: nextcord.Member):
        try:  
            embed= nextcord.Embed(title=member,description=f"ID: {member.id}")
            embed.add_field(name="Joined Discord", value=member.created_at.strftime("**Date:** %d/%m/%Y **Time:** %H:%M:%S"), inline=False)
            embed.add_field(name="Roles", value=", ".join([role.mention for role in member.roles]), inline=False)
            embed.add_field(name="Badges", value=", ".join([badge.name for badge in member.public_flags.all()]), inline=False)
            embed.add_field(name="Activity", value=member.activity, inline=False)
            embed.set_thumbnail(url=member.avatar.url)
            await interaction.response.send_message(embed=embed)
        except:
            embed=nextcord.Embed(description="```You cannot see this users info or user may be offline```")
            await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(mybot5(bot))