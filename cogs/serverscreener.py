# This is the server screening module, commands are built to warn a server when a flagged user joins.

# Import Stack
#from discord.channel import CategoryChannel
#from discord.ext import commands
#from discord.ext.commands import has_permissions
#import discord
#from discord.utils import get
#import discord.abc
import csv
import pathlib as pl

# Variables

flagged_users = pl.Path("userlist.csv")
flagged_user_dict = {}

# Set Up
if flagged_users.exists():
    with open("userlist.csv", newline="") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=["uuid", "justification"])
        for row in csvreader:
            flagged_user_dict.update({int(row["uuid"]):row["justification"]})
else:
    open("userlist.csv", "x")

print(flagged_user_dict)
