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
        targetid = target.id
        usermessages = await channel.history().flatten()
        for x in usermessages:
            if x.author.id == targetid:
                ctx.send(str(target)+" sent: "+x.content+" in "+str(channel)+" on "+x.created_at)

def setup(bot):
    bot.add_cog(sidewinder(bot))
