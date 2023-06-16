'''
Third version of text game 'Looking around' implementing movement of player
Author: Joao Pedro Amaral Pereira
Date: March 20, 2023
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


def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current_pos = [i,j]
            #different print if current position is where the player is
            if is_inside_grid(grid,current_pos) and current_pos != player_position:
                print(f'{grid[i][j]}', end='')
            else:
                print(f'@', end='')
        print('')


def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    num_rows = int(len(grid))
    num_cols = int(len(grid[0]))
    size_grid = [num_rows, num_cols]
    return size_grid


def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    row_pos = position[0]
    col_pos = position[1]
    valid = False
    if (row_pos < grid_rows) and (row_pos >= 0):
        if (col_pos < grid_cols) and (col_pos >= 0):
            valid = True
    return valid


def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]) and grid[row - 1][col] in allowed_objects:
        directions.append('north')
    if is_inside_grid(grid, [row, col - 1]) and grid[row][col - 1] in allowed_objects:
        directions.append('west')
    if is_inside_grid(grid, [row + 1, col]) and grid[row + 1][col] in allowed_objects:
        directions.append('south')
    if is_inside_grid(grid, [row, col + 1]) and grid[row][col + 1] in allowed_objects:
        directions.append('east')
    return directions

def print_directions(allowed_directions: list[str]) -> None:
    """
    Prints the allowed directions for the player to move to.
    """
    print(f'You can go ', end='')
    i = 0
    while i < len(allowed_directions):
        print(f'{allowed_directions[i]}', end=' ')
        i += 1
    print('')


def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    move_valid = False
    allowed_moves = look_around(grid, player_position)
    if direction in allowed_moves:
        move_valid = True
        if direction == 'west':
            player_position = [player_position[0],player_position[1] - 1]
        elif direction == 'east':
            player_position = [player_position[0],player_position[1] + 1]
        elif direction == 'north':
            player_position = [player_position[0] - 1,player_position[1]]
        elif direction == 'south':
            player_position = [player_position[0] + 1,player_position[1] + 1]
    return move_valid

    

def main():
    """
    Main entry point for the game.
    """
    #pull map from text file
    map_grid = load_map(MAP_FILE)
    #locate player start position
    player_pos = find_start(map_grid)
    #print directions player can go
    allowed_directions = look_around(map_grid, player_pos)
    print_directions(allowed_directions)
    #start game loop
    command = get_command()
    while command != 'escape':
        if command == "show map":
            display_map(map_grid,player_pos)
            print_directions(allowed_directions)
        elif command[0:2] == 'go':
            direction = command[3:]
            if move(direction, player_pos, map_grid):
                print(f'You moved {direction}.')
            else:
                "There is no way there."
        else:
            print(f'I do not understand.')
        command = get_command()


if __name__ == '__main__':
    main()