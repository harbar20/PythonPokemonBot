import json
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="b!")

with open("pokedex.json") as f:
    pokedexFile = json.load(f)
    pokedex = pokedexFile[0]





