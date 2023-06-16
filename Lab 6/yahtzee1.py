'''
A simplified version of the dice game Yahtzee 
v1
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

if __name__ == "__main__":
    main()