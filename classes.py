import pokebase as pb
    
class Pokemon():
    def __init__(self, pokemonName, nickname="", level="100", gender="F", isShiny=False,
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
        self.level = level
        self.gender = gender
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
    def get_level(self):
        return self.level
    def get_gender(self):
        return self.gender
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
    def change_level(self, newLevel):
        self.level = newLevel  
    def toggle_gender(self):
        if self.gender == 'F':
            self.gender == 'M'
        else:
            self.gender = 'F'      
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
        pass
    
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