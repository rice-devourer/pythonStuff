import discord
import os
from discord.ext import commands
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 

# Intents are required for Discord bots to function properly
intents = discord.Intents.default()
intents.message_content = True  # Enable if you want to read message content

# Create bot instance with a prefix (e.g., "!")
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: When bot is ready
@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# Command: Echo user input
@bot.command()
async def say(ctx, *, message: str):
    await ctx.send(message)

# Event: When a message is sent (optional)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Prevent bot from replying to itself

    if "hello" in message.content.lower():
        await message.channel.send("Hello there! 👋")

    # Process commands (required when overriding on_message)
    await bot.process_commands(message)



# Shutdown command (owner only)
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down... 🛑")
    await bot.close()

# Global error handler
@bot.event
async def on_command_error(ctx, error):
    print(f"❌ Error: {error}")  # Log error in terminal
    await ctx.send(f"⚠️ Error: {error}")  # Tell user

# Run bot (replace with your token)
bot.run(os.getenv("discord_bot_token"))
