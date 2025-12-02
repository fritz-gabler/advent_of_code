from typing import Literal
Direction = Literal["L", "R"]
Move = tuple[Direction, int]
DIAL_RANGE:tuple[int, int] = (0, 99)
def get_puzzel_input() -> list[str]:
    puzzel_input: list[str] = []

    with open("puzzel_input.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")
            puzzel_input.append(line)

    return puzzel_input
def create_moves(puzzle_input: list[str]) -> list[Move]:
    moves:list[Move] = []

    for line_input in puzzle_input:
        move = convert_input_line_to_move(line_input)
        moves.append(move)
    
    return moves
def convert_input_line_to_move(input:str) -> Move:
    direction:str
    number_of_moves:int
    move: Move

    direction = input[0]
    input = input.replace(direction, "")
    number_of_moves = int(input)
    move = (direction, number_of_moves)

    return move
