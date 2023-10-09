import nextcord
from nextcord.ext import commands
import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

class mybot2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Events is loaded")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"Message from {message.author} : {message.content}")
        if self.bot.user != message.author:
            if message.content.startswith(self.bot.user.mention):
                channel = message.channel
                response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                    "role": "assistant",
                    "content": "your name is Nix."
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
                text_to_send = response["choices"][0]["message"]["content"]
                await channel.send(text_to_send)
        
    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        await self.bot.get_channel(1054704591033335838).send(f"{member.mention} has joined the server")
    
def setup(bot):
    bot.add_cog(mybot2(bot))