import discord
from discord.ext import commands
import os, asyncio

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
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("discord_bot_token")) #runs bot

if __name__ == "__main__": #main method
    asyncio.run(main()) #runs everything
