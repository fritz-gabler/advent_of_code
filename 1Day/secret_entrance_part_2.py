from typing import Literal


DIAL_RANGE:tuple[int, int] = (0, 99)
DIAL_SIZE:int = DIAL_RANGE[1] - DIAL_RANGE[0] + 1

def main():
    lines: list[str] = get_puzzel_input()
    dial_turns: list[int] = create_dial_turns(lines)

    total_zero_clicks: int = 0
    current_dial_state: int = 50

    for line, dial_turn in zip(lines, dial_turns):
        zeros_this_move = count_zero_hits_for_move(current_dial_state, dial_turn)
        total_zero_clicks += zeros_this_move

        current_dial_state = turn_dial(current_dial_state, dial_turn)
    print("password (part 2):", total_zero_clicks)


def get_puzzel_input() -> list[str]:
    puzzel_input: list[str] = []

    with open("puzzel_input.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")
            puzzel_input.append(line)

    return puzzel_input

def create_dial_turns(puzzle_input: list[str]) -> list[int]:
    dial_turns:list[int] = []

    for line_input in puzzle_input:
        dial_turn:int = convert_input_line_to_dial_turn(line_input)
        dial_turns.append(dial_turn)
    
    return dial_turns

def convert_input_line_to_dial_turn(input:str) -> int:
    direction:str
    dital_turns: int

    direction = input[0]
    input = input.replace(direction, "")
    dital_turns = int(input)
    if direction == "L":
        dital_turns *= -1

    return dital_turns

def turn_dial(current_possition:int, dital_turn:int) -> int:
    current_possition += dital_turn
    current_possition = simulate_circular_behavior(current_possition)
    return (current_possition)

def simulate_circular_behavior(current_position:int) -> int:
    return current_position % DIAL_SIZE

def count_zero_hits_for_move(start_position: int, dial_step: int) -> int:
    if dial_step == 0:
        return 0

    step_direction = 1
    if dial_step < 0:
        step_direction = -1

    steps_to_take = abs(dial_step)

    if step_direction > 0:
        first_zero_step = (DIAL_SIZE - start_position) % DIAL_SIZE
    else:
        first_zero_step = start_position % DIAL_SIZE

    if first_zero_step == 0:
        first_zero_step = DIAL_SIZE

    if first_zero_step > steps_to_take:
        return 0

    additional_full_circles = (steps_to_take - first_zero_step) // DIAL_SIZE
    total_zero_hits = 1 + additional_full_circles
    return total_zero_hits

if __name__ == "__main__":
    main()
