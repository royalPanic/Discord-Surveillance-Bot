# This is the bulk collection module, commands are built to recall past messages by a user.

# Import Stack
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
from discord.utils import get
import discord.abc

# Module Code
class sidewinder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sidewind", hidden=True)
    @has_permissions(administrator=True)
    async def sidewind(self, ctx, target: discord.User, channel: discord.TextChannel):
        async for message in channel.history():
            if message.author == target:
                await ctx.send(str(target)+" sent: "+message.content+" in "+str(channel)+" on "+message.created_at.strftime("%m/%d/%Y, %H:%M:%S"))

def setup(bot):
    bot.add_cog(sidewinder(bot))
