'''
This a typing trainer game where you are rewarded by the speed in which you type 
the name of the spell, and if you get the name of the spell correct.
Author: Joao Pedro Amaral Pereira
Date:Feb 17, 2023
'''
import random
import time

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


def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    lower_input = user_input.lower()
    if spell == lower_input :
        print('Correct!')
    else:
        print('Incorrect! \nThe spell was: ' + spell)


def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """
    choice = input('Do you want to practice more? (y/n) \n')
    
    if choice.lower() == 'y':
        play = True
    else:
        play = False
    return play

def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    TTT = round(len(spell) * 0.3 ,2)
    return TTT
    # TODO: Implement this function

def calculate_points(spell: str, user_input: str, user_time: float,) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    answer: If answer is correct or incorrect
    """
    if spell == user_input:
        answer = True
    else:
        answer = False
    TTT = get_target_time(spell)
    points = 0
    if answer:
        if user_time <= TTT:
            points += 10
        elif user_time <= TTT * 1.5:
            points += 6
        elif user_time <= TTT * 2:
            points += 3
        else:
            points += 1
    else:
        points = -5

    return points
        
        
def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    # Game loop (call play_again())
    play = True
    final_score = 0
    #game loop
    while play == True:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        display_feedback(spell, user_input[0])
        points = calculate_points(spell, user_input[0], user_input[1])
        final_score += points
        print('You get ' + str(points) + ' points! Your score is: ' + str(final_score))
        play = play_again()
    print('Your final score is: '+ str(final_score))
    
main()