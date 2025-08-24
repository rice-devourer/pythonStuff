import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import pathlib
load_dotenv()

intents = discord.Intents.default() #set up needed intents
intents.message_content = True  
intents.members = True          
intents.guild_typing = True
intents.auto_moderation_configuration = True
intents.auto_moderation_execution = True
intents.dm_messages = True
intents.guild_messages = True
intents.guild_reactions = True

bot = commands.Bot(command_prefix="!", intents=intents) #get bot obj

@bot.event 
async def on_ready(): #ready event
    print(f"✅ Logged in as {bot.user}")

# loads all the cogs inside cogs
async def load_cogs():
    base_dir = pathlib.Path(__file__).parent
    cogs_dir = base_dir / "cogs"

    for path in cogs_dir.glob("*.py"):
        await bot.load_extension(f"cogs.{path.stem}")
        print(f"🔌 Loaded {path.stem}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("discord_bot_token")) #runs bot

if __name__ == "__main__": #main method
    asyncio.run(main()) #runs everything
