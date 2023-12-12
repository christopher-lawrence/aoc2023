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


def get_rows(entities: list[str]) -> list[Row]:
    """Parse the list of strings into Rows"""

    rows: list[Row] = []
    for entity in entities:
        print("parsing", entity)
        rows.append(parse_row(entity.strip("\r")))

    return rows


def get_lines(matrix: str) -> list[str]:
    """Split the string by newlines"""
    return matrix.split("\n")


def get_number_locations(row: str) -> list[Location]:
    """Get the number locations in the row"""
    locations: list[Location] = []
    for m in re.finditer(r"\d+", row):
        print(m.group(), m.start(), m.end())
        locations.append(Location(int(m.group()), m.start(), m.end() - 1))

    return locations


def get_symblol_locations(row: str) -> list[Location]:
    """Get the symbol locations in the row"""
    locations: list[Location] = []
    for m in re.finditer(r"[^\d|\.]", row):
        print(m.group(), m.start(), m.end())
        start = m.start() - 1 if m.start() > 0 else m.start()
        end = m.end() - 1 if m.end() == len(row) else m.end()
        locations.append(Location(m.group(), start, end))

    return locations


def parse_row(row: str) -> Row:
    """Parse the string into a Row"""
    numbers = get_number_locations(row)
    symbols = get_symblol_locations(row)

    return Row(numbers, symbols)


def find_valid_numbers(rows: list[Row]):
    """Find numbers with adjacent symbols"""
    index = 0
    values: list[int] = []

    # Steps
    # - Overlay each symbol in the current row
    # - If index > 0 overlay previous symbols onto current row
    # - If index > 0 overlay current symbols onto previous row

    for _ in range(len(rows)):
        intersecting = find_intersecting(rows[index].numbers, rows[index].symbols)
        if intersecting:
            values.extend(intersecting)

        if index == 0:
            index += 1
            continue

        previous_symbols = find_intersecting(
            rows[index].numbers, rows[index - 1].symbols
        )
        if previous_symbols:
            values.extend(previous_symbols)

        previous_numbers = find_intersecting(
            rows[index - 1].numbers, rows[index].symbols
        )
        if previous_numbers:
            values.extend(previous_numbers)

        index += 1

    return values


def find_gears(rows: list[Row]):
    index = 0
    values: list[int] = []

    for _ in range(len(rows)):
        for g in [gear for gear in rows[index].symbols if gear.value == "*"]:
            gear_values: list[int] = []

            gear_values.extend(find_intersecting(rows[index].numbers, [g]))

            if index < len(rows):
                gear_values.extend(find_intersecting(rows[index+1].numbers, [g]))
            
            if index > 0:
                gear_values.extend(find_intersecting(rows[index-1].numbers, [g]))

            if len(gear_values) == 2:
                values.append(gear_values[0] * gear_values[1])

        index += 1

    return values


def find_intersecting( numbers: list[Location], symbols: list[Location] ) -> list[int]:
    """Overlay the symbol ranges onto the number ranges to find intersections"""
    values: list[int] = []
    for symbol in symbols:
        s_range = range(symbol.start, symbol.end)
        for number in numbers:
            n_range = range(number.start, number.end)
            v = range(
                max(n_range.start, s_range.start), min(n_range.stop, s_range.stop)
            )
            if v.stop > v.start or v.stop == v.start:
                values.append(int(number.value))
    return values
