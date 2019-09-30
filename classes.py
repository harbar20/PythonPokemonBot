def importpokemon(pokemonstring):
    """
    Imports showdown pokemon and returns it as a PokemonClass instance.
    Code written by TheStraying11 (http://github.com/TheStraying11)
    """

    keys = ['Ability','Level','Shiny','Happiness','EVs','IVs']

    pokemon = {
        "Moves": []
    }
    first = pokemonstring.strip().split('\n')[0] # gets the first line of the input

    if len(first.split('@')) == 2: # checks for an item and adds it to the pokemon
        pokemon['Item'] = first.split('@')[1].strip()

    firstNoItem = first.split('@')[0] # gets the first line with the item removed

    if len(firstNoItem.split()) == 1:
        pokemon['Species'] = firstNoItem

    elif len(firstNoItem.split()) == 2: # deals with a case where there is only one parameter in brackets on the first line
        if firstNoItem.split()[1] in ['(M)', '(F)']: # checks whether parameter is gender
            pokemon['Gender'] = firstNoItem.split()[1][1:-1]
            pokemon['Species'] = firstNoItem.split()[0]
        else: # deals with the parameter being a species
            pokemon['Species'] = firstNoItem.split()[1][1:-1]
            pokemon['Nickname'] = firstNoItem.split()[0]
    elif len(firstNoItem.split()) == 3: # deals with the case where there is two parameters in the brackets on the first line
        pokemon['Nickname'] = firstNoItem.split()[0]
        pokemon['Species'] = firstNoItem.split()[1][1:-1]
        pokemon['Gender'] = firstNoItem.split()[2][1:-1]

    for i, line in enumerate(pokemonstring.strip().split('\n')): # loop for checking main body of the string
        if line.split(':')[0].strip() in keys: # this checks through the values listed in the 'keys' list
            pokemon[line.split(':')[0].strip()] = line.split(':')[1].strip()
        elif line.strip().startswith('-'): # checking for a line which contains Move data
            pokemon["Moves"].append(line.strip().replace('- ', ''))

        elif line.endswith('Nature'): # checking for a line which describes the Nature of the pokemon
            pokemon['Nature'] = line.strip().split()[0].strip()

    for k, v in pokemon.items():
        if k in ['EVs','IVs']: # performing additional operations on EVs and IVs
            pokemon[k] = v.split('/') # splits into individual stats
            pokemon[k] = [l.strip() for l in pokemon[k]] # strips each element
            pokemon[k] = dict(s.split()[::-1] for s in pokemon[k]) # converts the list into a dictionary


    if 'Shiny' in pokemon.keys(): # converts the 'Yes' that Showdown uses to a python Bool
        pokemon['Shiny'] = True
    else:
        pokemon['Shiny'] = False

    returnval = PokemonClass()

    for k, v in pokemon.items(): # sets the attributes of a PokemonClass instance to the values of the corresponding keys
        setattr(returnval, k, v)

    return returnval

class PokemonClass():
    def __init__(self, Moves = [], Item = '', Nickname = '', Species = '', Gender = '',
                Ability = '', Level = '100', Shiny = False, Happiness = '255', 
                EVs = {}, IVs = {}, Nature = ''):
        
        self.Moves = Moves
        self.Item = Item
        self.Nickname = Nickname
        self.Species = Species
        self.Gender = Gender
        self.Ability = Ability
        self.Level = Level
        self.Shiny = Shiny
        self.Happiness = Happiness
        self.EVs = EVs
        self.IVs = IVs
        self.Nature = Nature
    
    #accessor functions
    def get_Species(self):
        return self.Species
    def get_Nickname(self):
        return self.Nickname 
    def get_Gender(self):
        return self.Gender
    def get_Shiny(self):
        return self.Shiny
    def get_Happiness(self):
        return self.Happiness
    def get_Moves(self):
        return self.Moves
    def get_Item(self):
        return self.Item
    def get_Ability(self):
        return self.Ability
    def get_EVs(self):
        return self.EVs
    def get_IVs(self):
        return self.IVs
    def get_Nature(self):
        return self.Nature
    
    #mutator functions
    def change_nickname(self, newNickname):
        self.Nickname = newNickname 
    def toggle_Gender(self, newGender):
        self.Gender = newGender    
    def toggle_Shiny(self):
        if self.Shiny:
            self.Shiny = False
        else:
            self.Shiny = True
    def change_Happiness(self, newHappiness):
        self.Happiness = newHappiness
    def change_Move(self, oldMove, newMove):
        self.Moves[self.Moves.index(oldMove)] = newMove
    def change_Item(self, newItem):
        self.Item = newItem
    def change_Ability(self, newAbility):
        self.Ability = newAbility
    def change_EVs(self, evStat, evNum):
        self.EVs[evStat] = evNum
    def change_IVs(self, ivStat, ivNum):
        self.IVs[ivStat] = ivNum
    def change_Nature(self, newNature):
        self.Nature = newNature

class TeamClass():
    def __init__(self, team_name=''):
        self.team_name = team_name
        self.team = []
    
    def get_team(self):
        return self.team
    
    def get_team_name(self):
        return self.team_name
    
    def import_showdown_text(self, showdown_text):
        """
        Imports pokemon from showdown teams and appends them to self.team.
        Code written by TheStraying11 (http://github.com/TheStraying11)
        """
        showdown_text = showdown_text.strip().split('\n\n') # split into individual pokemon
        for i in showdown_text:
            pokemon = importpokemon(i) # create PokemonClass instance from the import string
            self.team.append(pokemon) # append the instance to the team list
    
    #TODO: port showdown's export code
    def export_showdown_text(self):
        """
        Effectively exports team in Showdown team format.
        """
        teamString = """"""
        
        #formatting it
        for pokemon in self.team:
            teamString += f"""
            {pokemon.get_Nickname()} ({pokemon.get_Species()}) ({pokemon.get_Gender()}) @ {pokemon.get_Item()}
            Ability: {pokemon.get_Ability()}
            Level: {pokemon.get_Level()}
            Shiny: {pokemon.get_Shiny}
            Happiness: {pokemon.get_Happiness()}
            EVs: {pokemon.get_EVs()}
            {pokemon.get_Nature()} Nature
            IVs: {pokemon.get_IVs}
            - {pokemon.get_Moves[0]}
            - {pokemon.get_Moves[1]}
            - {pokemon.get_Moves[2]}
            - {pokemon.get_Moves[3]}
            
            """
        
        return teamString
    
    def get_pokemon_info(self, pokemonID):
        return self.team[pokemonID+1]
    
    def change_team_name(self, newName):
        self.team_name = newName
    
    def add_pokemon(self, Moves = [], Item = '', Nickname = '', Species = '', Gender = 'F',
                Ability = '', Level = '100', Shiny = False, Happiness = '255', EVs = {}, IVs = {}, Nature = ''):        
        self.team[pokemonID+1] = PokemonClass(Moves, Item, Nickname, Species, Gender, Ability,
                                        Level, Shiny, Happiness, EVs, IVs, Nature)
    
    def remove_pokemon(self, pokemonID):
        self.team.pop(pokemonID+1)
    
    def change_nickname(self, pokemonID, newNickname):
        self.team[pokemonID+1].change_nickname(newNickname)

    def change_move(self, pokemonID, oldMove, newMove):
        selfTeam = self.get_team()
        self.team[pokemonID+1].moves[selfTeam.index(oldMove)] = newMove
    
    def change_item(self, pokemonID, item):
        self.team[pokemonID+1].change_item(item)
    
    def change_ability(self, pokemonID, newAbility):
        self.team[pokemonID+1].change_ability(newAbility)
    
    def change_ev(self, pokemonID, evStat, evNum):
        self.team[pokemonID+1].change_ev(evStat, evNum)
    
    def change_iv(self, pokemonID, ivStat, ivNum):
        self.team[pokemonID+1].change_iv(ivStat, ivNum)
    
    def change_nature(self, pokemonID, newNature):
        self.team[pokemonID+1].change_nature(newNature)