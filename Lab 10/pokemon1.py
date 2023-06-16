'''
First version of lab 10
Author: Joao Pedro Amaral Pereira
Date: april 5, 2023
References: None
'''

class Pokemon:
    def __init__ (self, name: str, attack: int, defense: int, max_health: int, current_health: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health
    


def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1.name} and {pokemon2.name}!")

if __name__ == '__main__':
    main()