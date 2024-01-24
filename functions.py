def print_desk(coords: list) -> None:
    """
    Prints the tic-tac-toe board with X and O symbols.
    Args:
        coords (list): List with coordinates of X and O.
    Returns:
        None
    """

    for row in range(3):
        for col in range(3):
            cell_empty = True
            for coord in coords:
                if col == coord['x'] and row == coord['y']:
                    print("X" if coord['player_x'] else "O", end=" ")
                    cell_empty = False
                    break
            if cell_empty:
                print("*", end=" ")
        print()