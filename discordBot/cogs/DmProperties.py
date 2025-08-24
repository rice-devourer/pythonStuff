from discord.ext import commands

class DMCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return ctx.guild is None   # must be in a DM

    @commands.command()
    async def secret(self, ctx):
        await ctx.send("works, dm message")

async def setup(bot):
    await bot.add_cog(DMCommands(bot))
