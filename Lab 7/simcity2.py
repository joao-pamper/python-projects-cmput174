'''
read and display land values from text file in an aligned format
Author: Joao Pedro Amaral Pereira
Date: March 17, 2023
References: f strings -> https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-literal_char ,
                        https://www.geeksforgeeks.org/string-alignment-in-python-f-string/ 
'''
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
                        neighbours.append(grid[r][c])
                    # elif c == col + 1:
                    #     neighbours.append(grid[r][c])
                    elif c == col and r != row:
                        neighbours.append(grid[r][c])
    return neighbours


def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_0.txt")
    print("Sim City Land Values:")
    display_grid(grid)


if __name__ == "__main__":
        main()