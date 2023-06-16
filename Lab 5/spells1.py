'''

Author: Joao Pedro Amaral Pereira
Date:
'''
import random

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    #read file into a list
    with open(filename, 'r') as file:
        text = file.readlines()
    #remove the '/n' from every item in the list
    index = 0
    for word in text:
        text[index] = word[0:len(word)-1]
        index += 1
        
    return text



def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    # TODO: implement this function
    random_num = random.randint(0, len(spells)-1)
    random_spell = spells[random_num]
    return random_spell.lower()
    



def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

main()

