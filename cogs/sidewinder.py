# This is the bulk collection module, commands are built to recall past messages by a user.

# Import Stack
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
from discord.utils import get
import discord.abc

# Module Code
class sidewinder(commands.cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sidewind", hidden=True)
    @has_permissions(administrator=True)
    async def sidewind(self, ctx, target: discord.User, channel: discord.TextChannel):
        targetid = target.id
        def IDcheck(message):
            return message.author.id == targetid
        usermessages = await channel.history(check=IDcheck).flatten()
        for x in usermessages:
            ctx.send(str(target)+" sent: "+x+" in "+channel)




# def check(message):
#     return message.author.id == some_author_id
#
# messages = await channel.history(limit=100, check=check).flatten()
#  Now you have 100 messages sent by a user
#  You can now iterate through every message and check whatever you want