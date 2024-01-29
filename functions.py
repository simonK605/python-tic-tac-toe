def check_winner(player_moves):
    # Check rows
    for i in range(3):
        if all(move in player_moves for move in [{'x': i, 'y': j, 'player_x': True} for j in range(3)]):
            return True

    # Check columns
    for j in range(3):
        if all(move in player_moves for move in [{'x': i, 'y': j, 'player_x': True} for i in range(3)]):
            return True

    # Check diagonals
    if all(move in player_moves for move in [{'x': i, 'y': i, 'player_x': True} for i in range(3)]) or \
       all(move in player_moves for move in [{'x': i, 'y': 2-i, 'player_x': True} for i in range(3)]):
        return True

    return False


def print_desk(coords: list) -> None:
    """
    Prints the tic-tac-toe board with X and O symbols.
    Args:
        coords (list): List with coordinates of X and O.
    Returns:
        None
    """

    win = False

    # Print the rows
    for row in range(3):
        # Print the columns
        for col in range(3):
            cell_empty = True

            # Check if the cell is empty
            for coord in coords:
                if col == coord['x'] and row == coord['y']:
                    print("X" if coord['player_x'] else "O", end=" ")
                    cell_empty = False
                    break

            if cell_empty:
                print("*", end=" ")
        print()

    player_x_moves = [player for player in coords if player['player_x']]
    player_y_moves = [player for player in coords if not player['player_x']]

    if check_winner(player_x_moves):
        print("Player X wins!")
    elif check_winner(player_y_moves):
        print("Player Y wins!")
    else:
        print("No winner yet.")

