# This is the wiretapping module, commands are built to track messages of one particular user.

#Import Stack
from discord.channel import CategoryChannel
from discord.ext import commands
from discord.ext.commands import has_permissions
import discord
from discord.utils import get
import discord.abc

#Variables
wiretapList = []

#Module Code
class wiretap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="startwiretap", aliases=["wiretap", "swt"], hidden=True)
    @has_permissions(administrator=True)
    async def startWiretap(self, ctx, user: discord.User):
        global wiretapList
        guild = ctx.message.guild
        category = get(guild.categories, name="Tickets")
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False)}

        if category is None:
            category = await guild.create_category_channel("Wiretaps")

        if user.id in wiretapList:
            await ctx.send("This user is already wiretapped.")
        else:
            wiretapList.append(user.id)
            channel = await guild.create_text_channel(str(user.id), category="Wiretaps", overwrites=overwrites)

    @commands.Cog.listener()
    async def on_message(anymessage):
        if message.author in wiretapList:
            if not isinstance(message.channel, discord.DMChannel):
                if get(guild.channels, name=str(anymessage.author.id)) is not None:
                    sendchannel = get(guild.channels, name=str(anymessage.author.id))
                    await sendchannel.send(anymessage.author.name+"sent:"+'"'+anymessage+'"'+"in "+anymessage.channel)

def setup(bot):
    bot.add_cog(wiretap(bot))
