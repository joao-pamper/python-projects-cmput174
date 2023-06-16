'''
A test file for the functions from the yahtzee game  
Author: Joao Pedro Amaral Pereira
Date: March 8, 2023
'''
from yahtzee2 import sum_of_given_number, fill_upper_section, num_of_a_kind, yahtzee

def test_sum_of_given_number_all_different():
    """
    Tests sum_of_given_number() with one roll
    where all dice have different face values.
    """
    roll = [1,2,3,4,5]
    assert sum_of_given_number(roll, 1) == 1
    assert sum_of_given_number(roll, 2) == 2
    assert sum_of_given_number(roll, 3) == 3
    assert sum_of_given_number(roll, 4) == 4
    assert sum_of_given_number(roll, 5) == 5
    assert sum_of_given_number(roll, 6) == 0
    

def test_sum_of_given_number_all_same():
    """
    Test sum_of_given_number() with one roll
    where all dice have the same face value.
    """
    roll = [1,1,1,1,1]
    # Assertions for all six values of `number`
    assert sum_of_given_number(roll, 1) == 5
    assert sum_of_given_number(roll, 2) == 0
    assert sum_of_given_number(roll, 3) == 0
    assert sum_of_given_number(roll, 4) == 0
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 0    
    
def test_sum_of_given_number_some_different():
    """
    Test sum_of_given_number() with one roll
    where some dice have the same face value.
    """
    roll = [1,1,1,6,4]
    # Assertions for all six values of `number`
    assert sum_of_given_number(roll, 1) == 3
    assert sum_of_given_number(roll, 2) == 0
    assert sum_of_given_number(roll, 3) == 0
    assert sum_of_given_number(roll, 4) == 4
    assert sum_of_given_number(roll, 5) == 0
    assert sum_of_given_number(roll, 6) == 6    

def test_fill_upper_section():
    """
    Test fill_upper_section() with any one roll of your choice.
    """
    roll = [1,1,1,1,1]
    assert fill_upper_section(roll) == [5,0,0,0,0,0]
    
def test_three_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "3 of a kind".
    """
    roll = [1,1,1,3,3]
    assert num_of_a_kind(roll, 3) == 9

def test_three_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "3 of a kind".
    """
    roll = [2,2,3,3,1]
    assert num_of_a_kind(roll, 3) == 0

def test_four_of_a_kind_found():
    """
    Tests num_of_a_kind() with a roll that has "4 of a kind".
    """
    roll = [4,4,4,4,6]
    assert num_of_a_kind(roll, 4) == 22

def test_four_of_a_kind_not_found():
    """
    Tests num_of_a_kind() with a roll that doesn't have "4 of a kind".
    """
    roll = [2,2,2,6,6]
    assert num_of_a_kind(roll, 4) == 0

def test_yahtzee_found():
    """
    Tests yahtzee() with a roll that has a yahtzee.
    """
    roll = [1,1,1,1,1]
    assert yahtzee(roll) == 50

def test_yahtzee_not_found():
    """
    Tests yahtzee() with a roll that has no yahtzee.
    """
    roll = [6,6,6,6,4]
    assert yahtzee(roll) == 0