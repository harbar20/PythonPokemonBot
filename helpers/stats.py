import json
from classes import PokemonClass
import math

#importing natures.json
with open("natures.json") as f:
    naturesList = json.load(f)

#changes the stats of the pokemon based on its nature
def stat_calc(pokemon):
    #checks if pokemon is of type PokemonClass
    if not isinstance(pokemon, PokemonClass):
        return None
    
    #saves all relevant info about the pokemon
    nature = pokemon.get_Nature()
    evDict = pokemon.get_EVs()
    ivDict = pokemon.get_IVs()
    stats = pokemon.get_Stats()
    level = pokemon.get_Level()
    
    #gets the info about the nature
    natureInfo = naturesList[nature]
    
    #performs the final stat calculation
    for statName, statValue in stats.items():
        #gathering individual data
        ev = evDict[statName]
        iv = ivDict[statName]
        natureFactor = natureInfo[statName]
        #doing the calc
        if statName == "HP":
            stats[statName] = math.floor(((2*statValue + iv + math.floor(ev/4))*level)/100) + level + 10
        else:
            stats[statName] = math.floor(((((2*statValue + iv + math.floor(ev/4))*level)/100) + 5) * natureFactor)
        #changing the actual pokemon stat
        pokemon.change_Stats(statName, stats[statName])
    
    return pokemon