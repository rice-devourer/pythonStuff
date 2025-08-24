from discord.ext import commands

class GuildProperties(commands.Cog):
    def __init__(self, bot): #setup commands class
        self.bot = bot

    async def cog_check(self, ctx):
        return ctx.guild is not None  # must be inside a guild

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"👋 Hello, {ctx.author.display_name} (in a server)")

async def setup(bot):
    await bot.add_cog(GuildProperties(bot))
