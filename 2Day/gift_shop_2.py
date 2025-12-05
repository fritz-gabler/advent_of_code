import re
Range = tuple[str, str]

def main():
    file_intput:str = get_file_input()
    sepreated_ranges:list[Range] = create_seperated_ranges(file_intput)
    all_invalid_ids:list[int] = get_all_invalid_ids(sepreated_ranges)
    added_awnser = add_all_invalid_ids(all_invalid_ids)
    print(added_awnser)
    

def get_file_input() -> str:
    file_input: str = ""

    with open("ids.txt") as file:
        file_input:str = file.read().rstrip('\n')
    return file_input

def create_seperated_ranges(file_input: str) -> list[Range]:
    seperated_ranges: list[Range] = []
    ranges: list[str]
    
    ranges = get_ranges(file_input)
    seperated_ranges = get_seperated_ranges(ranges)
    return seperated_ranges

def get_ranges(file_input: str) -> list[str]:
    return file_input.split(',')

def get_seperated_ranges(ranges: list[str]) -> list[Range]:
    seperated_ranges: list[Range] = []

    for one_range in ranges:
        split_range = one_range.split('-')
        range: Range = (split_range[0], split_range[1])
        seperated_ranges.append(range)

    return (seperated_ranges)

def get_all_invalid_ids(ranges: list[Range]) -> list[int]:
    invalid_ids: list[int] = []

    for range in ranges:
        all_id_from_range:list[str] = get_all_ids_from_range(range)
        invaild_ids_from_range:list[int] = get_invalid_ids_from_range(all_id_from_range)
        invalid_ids.extend(invaild_ids_from_range)
    return invalid_ids


def get_all_ids_from_range(range: Range) -> list[str]:
    current: int = int(range[0])
    end: int = int(range[1])
    all_ids_from_range: list[str] = []

    while current <= end:
        all_ids_from_range.append(str(current))
        current += 1

    return all_ids_from_range

def get_invalid_ids_from_range(all_ids_from_range: list[str]) -> list[str]:
    regex = r'^(\d+)\1+$'
    pattern = re.compile(regex)

    invalid_ids = []

    for id_str in all_ids_from_range:
        match = pattern.fullmatch(id_str)
        if match:
            print(match)  # show test output
            invalid_ids.append(id_str)

    return invalid_ids

def add_all_invalid_ids(all_invalid_ids: list[int]) -> int:
    added_id: int = 0

    for id in all_invalid_ids:
        added_id += int(id)

    return added_id

if __name__ == "__main__":
    main()
