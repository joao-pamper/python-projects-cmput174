'''
A simplified version of the dice game Yahtzee 
Author: Joao Pedro Amaral Pereira
Date: March 8, 2023
References: count() -> https://www.w3schools.com/python/ref_list_count.asp 
'''
import random
def make_roll() -> tuple:
    """
    Returns a tuple of five random values between 1 and 6.
    """
    roll = []
    while len(roll) < 5:
        roll.append(random.randint(1,6))
        
    return tuple(roll)


def sum_of_given_number(roll: tuple, number: int) -> int:
    """
    Returns the sum of the values in the roll that match the given number.
    """
    rep = roll.count(number)
    rep_sum = rep * number
    
    return rep_sum
            
    


def fill_upper_section(roll: tuple) -> list:
    """
    Returns a list of the sums of all values in the roll.
    """
    sums_list = []
    for i in range(1,7):
        sums = sum_of_given_number(roll, i)
        sums_list.append(sums)
        
    return sums_list


def display_upper_section(upper_section_scores: list) -> None:
    """
    Displays the upper section.
    """
    dice_names = ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']
    for i in range(6):
        print(str(dice_names[i]) + ': ' + str(upper_section_scores[i]))
        
        
def num_of_a_kind(roll: tuple, number: int) -> int:
    """
    If a roll has EXACTLY `number` dice of the same face value,
    returns the sum of all five values in the roll.
    Otherwise, returns 0.
    """
    # use sums_list to check if any number appears 'number' times
    sums_list = fill_upper_section(roll)
    i = 0
    of_a_kind = False
    while i <= 5:
        if sums_list[i] / (i +1) == number:
            of_a_kind = True
            i = 6
        i += 1
    # only sum upp roll if there is a combination
    if of_a_kind:
        sums = sum(roll)
    else:
        sums = 0
        
    return sums  


def yahtzee(roll: tuple) -> int:
    """
    Returns 50 if the roll is a Yahtzee (all dice in the roll have the same
    face value). Otherwise, returns 0.
    """
    sums_list = fill_upper_section(roll)
    i = 0
    points = 0
    while i <= 5:
        if sums_list[i] / (i +1) == 5:
            i = 6
            points = 50
        i += 1
    
    return points


def main():
    """
    Main function.
    """
    # Roll the dice (and print as in demo)
    roll = make_roll()
    print('Rolling the dice... ' + str(roll))
    # Fill the upper section
    sums_list = fill_upper_section(roll)
    # Display the upper section
    print('Upper section:')
    display_upper_section(sums_list)
    # Display the lower section
    print('Lower section:')
    # Calculate and display "3 of a kind" for the given roll
    print('Three of a kind: ' + str(num_of_a_kind(roll, 3)))
    # Calculate and display "4 of a kind" for the given roll
    print('Four of a kind: ' + str(num_of_a_kind(roll, 4)))
    # Calculate and display "Yahtzee" for the given roll
    print('Yahtzee: ' + str(yahtzee(roll)))

if __name__ == "__main__":
    main()