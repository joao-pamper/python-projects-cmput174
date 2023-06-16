'''
Third version of lab 10
Author: Joao Pedro Amaral Pereira
Date: april 6, 2023
References: None
'''
import random

class Pokemon:
    def __init__ (self, name: str, attack: int, defense: int, max_health: int, current_health: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health
    
    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        pokemon_str = self.name+' (health: '+str(self.current_health)+'/'+str(self.max_health)+')'
        return pokemon_str

    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount < 0:
            pass
        elif amount < self.current_health:
            self.current_health -= amount
        elif amount >= self.current_health:
            self.current_health = 0    
        
    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        alive = False
        if self.current_health > 0:
            alive = True
        return alive

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        if self.current_health == 0:
            self.current_health = self.max_health

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    with open(filename, 'r', encoding ='utf-8') as file:
        text = file.read().splitlines()
    #remove first line
    text.remove('Name|Attack|Defense|Health')
    # split info for easy access, creating a 2D list of strings
    for i in range(len(text)):
        text[i] = text[i].split('|')
    return text




def main():
    """
    Battle of two Pokemon
    """
    filename = 'all_pokemon.txt'
    #read file
    pokemon_file = read_pokemon_from_file(filename)
    # find random different pokemons
    r1 = random.randint(0,801)
    r2 = random.randint(0,801)
    while r1 == r2:
        r2 = random.randint(0,802)
    #assign them to pokemon class using info from file
    pokemon1 = Pokemon(pokemon_file[r1][0], int(pokemon_file[r1][1]), int(pokemon_file[r1][2]), int(pokemon_file[r1][3]), int(pokemon_file[r1][3]))
    pokemon2 = Pokemon(pokemon_file[r2][0], int(pokemon_file[r2][1]), int(pokemon_file[r2][2]), int(pokemon_file[r2][3]), int(pokemon_file[r2][3]))
    print(f"Welcome, {pokemon1} and {pokemon2}!")

if __name__ == '__main__':
    main()