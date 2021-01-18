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
    async def startWiretap(self, ctx, pinguser: discord.User):
        global wiretapList
        guild = ctx.message.guild
        category = get(guild.categories, name="FISA Court")
        categoryid = get(guild.categories, name="FISA Court").id
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False)}
        userid = pinguser.id

        if category is None:
            category = await guild.create_category_channel("FISA Court")
            categoryid = get(guild.categories, name="FISA Court").id


        if userid in wiretapList:
            await ctx.send("This user is already wiretapped.")
        else:
            wiretapList.append(userid)
            await ctx.send("FISA Warrant Approved, Wiretap Opened.")
            if get(guild.channels, name=str(userid)) is None:
                await guild.create_text_channel(name=userid, category=category, overwrites=overwrites)


    @commands.command(name="closewiretap", aliases=["endwiretap","cwt","ewt"], hidden=True)
    @has_permissions(administrator=True)
    async def endWiretap(self, ctx, pinguser: discord.User):
        global wiretapList
        if pinguser.id in wiretapList:
            wiretapList.remove(pinguser.id)
            await ctx.send("That user's wiretap has been closed.")
        else:
            await ctx.send("That user is not wiretapped.")

    @commands.Cog.listener()
    async def on_message(self, given_message):
        guild = given_message.guild
        if given_message.author.id in wiretapList:
            #print("Message from wiretap flagged user.")
            if not isinstance(given_message.channel, discord.DMChannel):
                #print("AND not a DM.")
                if get(guild.channels, name=str(given_message.author.id)) is not None:
                    #print("AND user has an existing wiretap channel.")
                    sendchannel = get(guild.channels, name=str(given_message.author.id))
                    await sendchannel.send(str(given_message.author.name)+" sent: "+'`'+str(given_message.content)+'`'+" in "+str(given_message.channel.name))

def setup(bot):
    bot.add_cog(wiretap(bot))