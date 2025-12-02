from typing import Literal

Direction = Literal["L", "R"]

Move = tuple[Direction, int]
DIAL_RANGE:tuple[int, int] = (0, 99)


def main():
    input:list[str] = get_puzzel_input()
    moves: list[Move] = create_moves(input)
    number_of_zeros: int = 0;
    current_dial_state: int = 50

    print("The dial starts by pointing at ", current_dial_state)
    for move in moves:
        current_dial_state = turn_dial(current_dial_state, move)
        input_line = move[0] + str(move[1])
        print("The dial is rotated ", input_line, " to point at ", current_dial_state)
        if current_dial_state == 0:
            number_of_zeros += 1
    print("Total number of the state 0: ", number_of_zeros)




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

def turn_dial(current_possition:int, move:Move) -> int:
    if move[0] == "R":
        current_possition += move[1] 
    elif move[0] == "L":
        current_possition -= move[1] 
    current_possition = simulate_circular_behavior(current_possition)

    return (current_possition)

def simulate_circular_behavior(current_possition) -> int:
    if current_possition > DIAL_RANGE[1]:
        current_possition -= 100
    elif current_possition < DIAL_RANGE[0]:
        current_possition += 100
    return current_possition

if __name__ == "__main__":
    main()
