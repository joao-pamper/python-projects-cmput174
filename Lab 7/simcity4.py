'''
Read and display land values from text file in an aligned format, calculate values for '0', and display stats
Author: Joao Pedro Amaral Pereira
Date: March 17, 2023
References: f strings -> https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-literal_char ,
                        https://www.geeksforgeeks.org/string-alignment-in-python-f-string/ 
            deepcopy -> https://docs.python.org/3/library/copy.html
'''
import copy

def create_grid(filename: str) -> list[list[int]]:
    """
    Create a grid of land values from a file
    """
    # Open file and save as text_raw
    with open(filename, 'r') as file:
        text_raw = file.readlines()
    # Make a list without the first two values and without '/n' and save as text_ready
    text_ready = []
    for index in range(2,len(text_raw)):
        item = text_raw[index]
        text_ready.append(item[0:len(item)-1] )    
    # Create the 2D list called grid
    grid = []
    rows = int(text_raw[0])
    columns = int(text_raw[1])
    for i in range(rows):
        grid.append(text_ready[i*rows: i*rows+columns])
    return grid
        

def display_grid(grid: list[list[int]]) -> None:
    """
    Display a grid of land values
    """
    for row in grid:
        print(f'{row[0]:>8}', end="")
        for value in row[1:]:
            print(f'{value:>9}', end="")
        print('') #will make the next row start in next line


def find_neighbor_values(grid: list[list[int]], row: int, col: int) -> list[int]:
    """
    Find the neighbors of a cell
    """
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    neighbours = []
    for r in range(max_row + 1):
            #check if row is possible
            if r == row -1 or r == row or r == row +1:
                for c in range(max_col + 1):
                    if c == col - 1 or c == col + 1:
                        neighbours.append(int(grid[r][c]))
                    elif c == col and r != row:
                        neighbours.append(int(grid[r][c]))
    return neighbours


def fill_gaps(grid: list[list[int]]) -> list[list[int]]:
    """
    Fill the gaps in the grid
    Creates a new grid with the same dimensions as the original grid
    Calls find_neighbor_values() to find the neighbors of each cell
    Do NOT modify the original grid!
    """
    copy_grid = copy.deepcopy(grid)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if int(grid[row][col]) == 0:
                neighbours = find_neighbor_values(grid,row,col)
                estimate = sum(neighbours)/(len(neighbours))
                copy_grid[row][col] = round(estimate)


    return copy_grid
    
    
def find_max(grid: list[list[int]]) -> int:
    """
    Find the max value in the grid (rounded to the nearest integer)
    """
    max_value = [0]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if int(grid[row][col]) > int(max_value[0]):
                max_value[0] = round(int(grid[row][col]))
    return max_value[0]

def find_average(grid: list[list[int]]) -> int:
    """
    Find the average value in the grid (rounded to the nearest integer)
    """
    flat_grid = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            flat_grid.append(int(grid[row][col]))
    average_value = sum(flat_grid)/(len(flat_grid))
    return round(average_value)
    
    
    
def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_3.txt")
    print("Sim City Land Values:")
    display_grid(grid)
    print("\nCalculated Sim City land values:")
    new_grid = fill_gaps(grid)
    display_grid(new_grid)
    print("\nSTATS")
    print(f"Average land value in this city: {find_average(new_grid)}")
    print(f"Maximum land value in this city: {find_max(new_grid)}")



if __name__ == "__main__":
        main()