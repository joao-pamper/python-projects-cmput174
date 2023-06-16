'''
Minimum version of text game
Author: Joao Pedro Amaral Pereira
Date: March 20, 2022
References:
'''

MAP_FILE = 'cave_map.txt'

def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    #read file
    with open(map_file, "r") as file:
        text = file.read().splitlines()
    #create grid from text
    grid = []
    for i in range(len(text)):
        row = []
        for j in range(len(text[i])):
            row.append(text[i][j])
        grid.append(row)
    return grid


def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    found = False
    while not found:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S':
                    found = True
                    start_pos = [int(i),int(j)]
        found = True # to prevent infinite iteration
    return start_pos

def get_command() -> str:
    """
    Gets a command from the user.
    """
    command = input()
    return str(command)


def main():
    """
    Main entry point for the game.
    """
    map_grid = load_map(MAP_FILE)
    print(map_grid)
    start_pos = find_start(map_grid)
    print(f'Starting position: {start_pos}')
    command = get_command()
    while command != 'escape':
        print(f'I do not understand.')
        command = get_command()


if __name__ == '__main__':
    main()
