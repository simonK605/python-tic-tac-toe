from functions import print_desk


def start(player_x: bool) -> dict:
    """
    Start the game.
    Args:
        player_x (bool): True if it's player X's turn.
    Returns:
        dict: Coordinates of X and O.
    """
    while True:
        # Get the coordinates
        coord_x = int(input(f"Player {'X' if player_x else 'O'} please enter x coordinate from 1 to 3: "))
        coord_y = int(input(f"Player {'X' if player_x else 'O'} please enter y coordinate from 1 to 3: "))

        if coord_x <= 0 or coord_x > 3 or coord_y <= 0 or coord_y > 3:
            print("You should enter numbers from 1 to 3")
        else:
            # The desk is 3x3 and coordinates start from 0, so we need to subtract 1
            return {"x": coord_x - 1, "y": coord_y - 1, "player_x": player_x}


def game():
    # List of coordinates
    coords_list = []

    # First player is X (True is X)
    player_x = True

    while True:
        coords = start(player_x)
        is_same_coord = False
        for coord in coords_list:
            if coord['x'] == coords['x'] and coord['y'] == coords['y']:
                print("This cell is already occupied. Choose another one!")
                is_same_coord = True
                break

        if is_same_coord:
            continue

        coords_list.append(coords)
        print_desk(coords_list)
        player_x = not player_x


# May the best player win :)
game()

