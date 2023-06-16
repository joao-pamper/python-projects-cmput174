'''
Second version of lab 10
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



def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1} and {pokemon2}!")

if __name__ == '__main__':
    main()