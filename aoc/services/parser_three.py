# Example:
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

import re


class Location:
    def __init__(self, value: int | str, start: int, end: int):
        self.value = value
        self.start = start
        self.end = end

    def __eq__(self, value) -> bool:
        return (
            self.value == value.value
            and self.start == value.start
            and self.end == value.end
        )


class Row:
    def __init__(self, numbers: list[Location], symbols: list[Location]):
        self.numbers = numbers
        self.symbols = symbols

    def __eq__(self, value) -> bool:
        return self.numbers == value.numbers and self.symbols == value.symbols


def get_lines(matrix: str) -> list[str]:
    return matrix.split("\n")


def get_number_locations(row: str) -> list[Location]:
    print(row)
    locations: list[Location] = []
    for m in re.finditer(r"\d+", row):
        print(m.group(), m.start(), m.end())
        locations.append(Location(int(m.group()), m.start(), m.end() - 1))

    return locations


def get_symblol_locations(row: str) -> list[Location]:
    print(row)
    locations: list[Location] = []
    for m in re.finditer(r"[^\d|\.]", row):
        print(m.group(), m.start(), m.end())
        locations.append(Location(m.group(), m.start(), m.end() - 1))

    return locations


def parse_row(row: str) -> Row:
    numbers = get_number_locations(row)
    symbols = get_symblol_locations(row)

    return Row(numbers, symbols)

def find_valid_numbers(rows: list[Row]) -> list[int]:
    pass
