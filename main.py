import pokebase as pb
import discord
from discord.ext import commands
from classes import Pokemon, Team

bot = commands.Bot(command_prefix="b!")

@bot.event
async def on_connect():
    print("Showdown Bot is online!")

@bot.command()
async def createTeam(ctx, teamName):
    """
    Creates a team.
    """
    