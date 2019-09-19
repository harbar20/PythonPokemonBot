import pokebase as pb

#getting a list of all pokemon names currently
with open("pokemon_names.txt") as f:
    pokemon = [i.replace("\n", "") for i in f]
    
#function to find nth instance of substring in a string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
    
class Pokemon():
    def __init__(self, pokemonName, nickname="", isShiny=False,
                moves=["", "", "", ""], item="", ability="",
                EVs={"HP":0,
                     "Atk":0,
                     "Def":0,
                     "SpA":0,
                     "Spd":0,
                     "Spe":0
                    }, 
                IVs={"HP":0,
                     "Atk":0,
                     "Def":0,
                     "SpA":0,
                     "Spd":0,
                     "Spe":0
                    }, nature=""):
        self.name = pokemonName
        self.nickname = nickname
        self.isShiny = isShiny
        self.moves = moves
        self.item = item
        self.ability = ability
        self.ev = EVs
        self.iv = IVs
        self.nature = nature
        
    def get_name(self):
        return self.name
    def get_nickname(self):
        return self.nickname 
    def get_isShiny(self):
        return self.isShiny
    def get_moves(self):
        return self.moves
    def get_item(self):
        return self.item
    def get_ability(self):
        return self.ability
    def get_ev(self):
        return self.ev
    def get_iv(self):
        return self.iv
    def get_nature(self):
        return self.iv
    
    def change_nickname(self, newNickname):
        self.nickname = newNickname      
    def toggle_isShiny(self):
        if self.isShiny:
            self.isShiny = False
        else:
            self.isShiny = True
    def change_move(self, oldMove, newMove):
        self.moves[self.moves.index(oldMove)] = newMove
    def change_item(self, newItem):
        self.item = newItem
    def change_ability(self, newAbility):
        self.ability = newAbility
    def change_ev(self, evStat, evNum):
        self.ev[evStat] = evNum
    def change_iv(self, ivStat, ivNum):
        self.iv[ivStat] = ivNum
    def change_nature(self, newNature):
        self.nature = newNature
    
class Team():
    def __init__(self, team_name):
        self.team_name = team_name
        self.team = {}
    
    def get_team(self):
        return self.team
    
    def get_team_name(self):
        return self.team_name
    
    def import_showdown_text(self, showdown_text):
        """
        Imports showdown teams and saves it as the team.
        """
        #separating the text by pokemon
        pokemonTextList = showdown_text.split("\n\n")
        
        #going through each pokemon data in the list
        for pokemonData in pokemonTextList:
            counter = 2
            #getting name/nickname from pokemon
            currentIndex = pokemonData.find("@") - 1
            name = pokemonData[:currentIndex]
            #looking through list of all pokemon names to see if they have nicknames
            if name not in pokemon:
                nickname = name[:pokemonData.find("(") - 1]
                name = name[pokemonData.find("(")+1:pokemonData.find(")")]
            else:
                nickname = ""
            #print("Nickname: ", currentIndex)
            
            #getting the item of the pokemon
            currentIndex += 3
            item = pokemonData[currentIndex:pokemonData.find("\n")]
            #print("Item: ", currentIndex)
            
            #getting the ability of the pokemon
            currentIndex = pokemonData.find("\n") + 10
            ability = pokemonData[currentIndex:find_nth(pokemonData, "\n", counter)]
            #print("Ability: ", currentIndex)
            
            #checking if the pokemon is shiny
            currentIndex = find_nth(pokemonData, "\n", counter) + 1
            if pokemonData[currentIndex:currentIndex + 5] == 'Shiny':
                isShiny = True
                currentIndex += 13
                counter = 4
            else:
                isShiny = False
                currentIndex += 1#to be changed soon
                counter = 3
            
            #print("Shiny: ", currentIndex)
            
            #getting the pokemon's EV's
            currentIndex += 5
            EVs = pokemonData[currentIndex:find_nth(pokemonData, "\n", counter)]
            
            #getting the pokemon's nature
            currentIndex = find_nth(pokemonData, "\n", counter) + 1
            nature = pokemonData[currentIndex:find_nth(pokemonData, "\n", counter+1)]
            nature = nature[:-8]
            counter += 1
            
            #print("Nature: ", nature)
            
            #getting the pokemon's IV, if any
            currentIndex = find_nth(pokemonData, "\n", counter) + 1
            if pokemonData[currentIndex:currentIndex+3] == "IVs":
                counter += 1
                IVs = pokemonData[currentIndex+5:find_nth(pokemonData, "\n", counter)]
                currentIndex = find_nth(pokemonData, "\n", counter)
            else:
                IVs = ""
                currentIndex = find_nth(pokemonData, "\n", counter)
            
            #print("IVs: ", IVs)
        
            #getting the pokemon's moves
            currentIndex = find_nth(pokemonData, "\n", counter) + 1
            newPokemonData = pokemonData[currentIndex:]
            moves = []
            for i in newPokemonData.split("\n"):
                moves.append(i[2:-2])
            
            #print("Moves: ", moves)
        
            #finally putting all the info into a .json format for visualization
            newText = {"name":name, "nickname":nickname, "item":item, "ability":ability,
                       "shiny": isShiny, "evs": EVs, "nature":nature, "ivs": IVs, "moves":moves}
            
            #adding a Pokemon class to the team with all these attributes
            self.team[name] = Pokemon(name, nickname, item, ability, 
                                      isShiny, EVs, nature, IVs, moves)
    
    def export_showdown_text(self):
        """
        Effectively exports team in Showdown team format.
        """
        pass
    
    def get_pokemon_info(self, pokemonName):
        return self.team[pokemonName]
    
    def change_team_name(self, newName):
        self.team_name = newName
    
    def add_pokemon(self, pokemonName, nickname="", level="100", gender="F", isShiny=False,
                    moves=[], item="", ability="",
                    EVs={}, IVs={}, nature=""):        
        self.team[pokemonName] = Pokemon(pokemonName, nickname, level, gender, isShiny,
                                         moves, item, ability,
                                         EVs, IVs, nature)
    
    def remove_pokemon(self, pokemonName):
        self.team.remove(pokemonName)
    
    def change_nickname(self, pokemonName, newNickname):
        self.team[pokemonName].change_nickname(newNickname)

    def change_move(self, pokemonName, oldMove, newMove):
        selfTeam = self.get_team()
        self.team[pokemonName].moves[selfTeam.index(oldMove)] = newMove
    
    def change_item(self, pokemonName, item):
        self.team[pokemonName].change_item(item)
    
    def change_ability(self, pokemonName, newAbility):
        self.team[pokemonName].change_ability(newAbility)
    
    def change_ev(self, pokemonName, evStat, evNum):
        self.team[pokemonName].change_ev(evStat, evNum)
    
    def change_iv(self, pokemonName, ivStat, ivNum):
        self.team[pokemonName].change_iv(ivStat, ivNum)
    
    def change_nature(self, pokemonName, newNature):
        self.team[pokemonName].change_nature(newNature)
    
team = Team("IGL Pokemon Team")