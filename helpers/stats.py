import json
from classes import PokemonClass
import math
import requests

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

def ability_stat_calc(pokemon):
    pass

def move_stat_calc(pokemon, moveUsed):
    #checks if pokemon is of type PokemonClass
    if not isinstance(pokemon, PokemonClass):
        return None
    
    #for stat changes for moves
    weirdStatNames = {"attack":"Att", 
                      "defense":"Def", 
                      "special-attack":"SpA", 
                      "special-defense":"SpD",
                      "speed":"Spe"}
    #stat change index to actual stat multiplier dictionary
    indexToMultiplier = {"-6":2/8,
                         "-5":2/7,
                         "-4":2/6,
                         "-3":2/5,
                         "-2":2/4,
                         "-1":2/3,
                         "0":2/2,
                         "1":3/2,
                         "2":4/2,
                         "3":5/2,
                         "4":6/2,
                         "5":7/2,
                         "6":8/2,}
    
    #saves info about the pokemon
    stats = pokemon.get_Stats()
    
    #gets the stat changes from the moves
    moveStatChanges = {}
    moveFormatted = moveUsed.lower().replace(" ", "-")
    r = json.load(requests.get(f'https://pokeapi.co/api/v2/move/{moveFormatted}'))
    for statChange in r["stat_changes"]:
        stats[weirdStatNames[statChange["stat"]["name"]]] *= indexToMultiplier[statChange["change"]]
    
    #changes the actual stats of the pokemon
    for statName, statValue in stats:
        pokemon.change_Stats(statName, statValue)