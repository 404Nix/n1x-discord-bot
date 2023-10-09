import nextcord
from nextcord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')

intents = nextcord.Intents.all()
intents.members= True
game = nextcord.Game("Cogs")
bot= commands.Bot(command_prefix=".", intents=intents)
#bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=nextcord.Status.idle, activity=nextcord.Game('with you mum'))
    print(f"Success : Bot has successfully logged in as {bot.user.name}")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"loaded {extension}")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}")


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}")

for i in os.listdir("./cogs"):
    if i.endswith(".py"):
        bot.load_extension(f"cogs.{i[:-3]}")
        #print(f"loaded cogs {i}")




bot.run(token)