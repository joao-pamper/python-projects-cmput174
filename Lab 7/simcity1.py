'''
Read and display land values from text file in an aligned format 
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
         
              
    


def main() -> None:
    """
    Main program.
    """
    grid = create_grid("data_3.txt")
    print("Sim City Land Values:")
    display_grid(grid)

if __name__ == "__main__":
        main()