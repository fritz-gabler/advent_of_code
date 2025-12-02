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
