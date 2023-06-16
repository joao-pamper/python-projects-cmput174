'''
Harry Potter typing trainer
Author: Joao Pedro Amaral Pereira
Date: Feb 14 2023
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
    

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    symbol = '#'
    print(60*symbol)
    print('Harry Potter Typing Trainer')
    print(60*symbol)


def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    #read file into a list
    with open('instructions.txt', 'r') as file:
        instructions = file.readlines()
    #remove the '/n' from every item in the list
    index = 0
    for word in instructions:
        instructions[index] = word[0:len(word)-1]
        index += 1
    #print each item from the list
    for item in instructions:
        print(item)


def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    user_input = input('Type the following spell: ' + spell + '\n')
    return user_input
    

def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    lower_input = user_input.lower()
    if spell == lower_input :
        print('Correct!')
    else:
        print('Incorrect! \nThe spell was: ' + spell)


def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)


main()


