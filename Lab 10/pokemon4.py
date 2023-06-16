'''
Final version of lab 10
Simulates a pokemon battle between two randomly chosen pokemon.
Author: Joao Pedro Amaral Pereira
Date: april 8, 2023
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
        print(f'{self.name} has been revived!')
    
    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
        This method can either return a bool, or return nothing
        (depends on your implementation)
        """
        attack_success = False
        luck = (random.randrange(70,130,10)) / 100
        damage = round(luck * float(self.attack))
        #print(luck)
        print(f'{self.name} attacks {other.name} for {damage} damage!')
        if damage <= other.defense:
            attack_success = False
            print(f'Attack is blocked!')
        else:
            attack_success = True
            other.lose_health(damage - other.defense)
            print(f'Attack is successfull! {other.name} has {other.current_health} health remaining!')
        return attack_success

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
    #start game loop
    round = 1
    while round <= 10:
        print('')
        print(f'Round {round} begins! {pokemon1} and {pokemon2}')
        #attack from pokemon 1 on 2
        pokemon1.attempt_attack(pokemon2)
        #if pokemon2 is dead attempt revive
        if pokemon2.is_alive() == False:
            revive_luck1 = random.choice([0,1]) # 1 will revive and 0 will not
            if revive_luck1 == 1:
                #revive dead pokemon
                pokemon2.revive()
                attack2 = pokemon2.attempt_attack(pokemon1)
            else:
                winner = pokemon1
                end_round = round
                round = 100
        #if pokemon2 still alive he will attack 1
        else:
            attack2 = pokemon2.attempt_attack(pokemon1)
        #if pokemon1 is dead attempt revive, else next round
        if pokemon1.is_alive() == False:
            revive_luck2 = random.choice([0,1])
            if revive_luck2 == 1:
                #revive dead pokemon
                pokemon1.revive()
                #next round
                round += 1
            else:
                winner = pokemon2
                end_round = round
                round = 100
        else:
            round += 1
    print('')
    if round >= 100:
        print(f'{winner} has won in {end_round} rounds!')
    else:
        print(f"It's a tie between {pokemon1} and {pokemon2}!")


if __name__ == '__main__':
    main()