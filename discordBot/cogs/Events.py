from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.id == "1205317617619963944":
            await message.channel.send("event works")

        # process commands so @bot.command works
        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(Events(bot))
