from django.test import TestCase

from .services.parser_three import (
    Location,
    Row,
    find_valid_numbers,
    get_lines,
    get_number_locations,
    get_symblol_locations,
    parse_row,
)

matrix = [
    "467..114..",#0
    "...*......",#1
    "..35..633.",#2
    "......#...",#3
    "617*......",#4
    ".....+.58.",#5
    "..592.....",#6
    "......755.",#7
    "...$.*....",#8
    ".664.598..",#9
    ".........9",#10
    "97$43.....",#11
    ".....98$44",#12
    "*.........",#13
    ".*.......*",#14
    "1.1.....56",#15
    "1.*.......",#16
]


matrix_str = "\n".join(matrix)


class ParserThreeTestCase(TestCase):
    def test_get_lines(self):
        result = get_lines(matrix_str)

        self.assertEqual(result[0], matrix[0])
        self.assertEqual(len(result), len(matrix))

    def test_get_number_locations(self):
        result = get_number_locations(matrix[0])

        expected: list[Location] = [Location(467, 0, 2), Location(114, 5, 7)]

        self.assertEqual(result, expected)

    def test_get_number_locations_end(self):
        result = get_number_locations(matrix[10])

        expected = [Location(9, 9, 9)]

        self.assertEqual(result, expected)

    def test_get_number_locations_mixed(self):
        result = get_number_locations(matrix[4])

        expected: list[Location] = [Location(617, 0, 2)]

        self.assertEqual(result, expected)

    def test_get_symbol_locations(self):
        result = get_symblol_locations(matrix[1])

        expected: list[Location] = [Location("*", 2, 4)]

        self.assertEqual(result, expected)

    def test_get_symbol_begin(self):
        result = get_symblol_locations(matrix[13])

        expected = [Location("*", 0, 1)]

        self.assertEqual(result, expected)

    def test_get_symbol_end(self):
        result = get_symblol_locations(matrix[14])

        expected = [Location("*", 0, 2), Location("*", 8, 9)]

        self.assertEqual(result, expected)

    def test_get_symbol_locations_mixed(self):
        result = get_symblol_locations(matrix[4])

        expected = [Location("*", 2, 4)]

        self.assertEqual(result, expected)

    def test_get_symbol_locations_many(self):
        result = get_symblol_locations(matrix[8])

        expected = [Location("$", 2, 4), Location("*", 4, 6)]

        self.assertEqual(result, expected)

    def test_parse_row(self):
        result = parse_row(matrix[0])

        expected = Row([Location(467, 0, 2), Location(114, 5, 7)], [])

        self.assertEqual(result, expected)

    def test_parse_row_mixed(self):
        result = parse_row(matrix[4])

        expected = Row([Location(617, 0, 2)], [Location("*", 2, 4)])

        self.assertEqual(result, expected)

    def test_find_valid_numbers_valid(self):
        row1 = parse_row(matrix[4])

        result = find_valid_numbers([row1])

        self.assertEqual(result, [617])

    def test_find_valid_numbers_invalid(self):
        row1 = parse_row(matrix[5])

        result = find_valid_numbers([row1])

        self.assertEqual(result, [])

    def test_find_valid_numbers_full(self):
        row4 = parse_row(matrix[4])
        row5 = parse_row(matrix[5])
        row6 = parse_row(matrix[6])

        result = find_valid_numbers([row4, row5, row6])

        self.assertEqual(result, [617, 592])

    def test_symbol_surrounded_begin(self):
        row11 = parse_row(matrix[11])

        result = find_valid_numbers([row11])

        self.assertEqual(result, [97, 43])

    def test_symbol_surrounded_end(self):
        row11 = parse_row(matrix[12])

        result = find_valid_numbers([row11])

        self.assertEqual(result, [98, 44])

    def test_full_test(self):
        rows: list[Row] = []
        for row in matrix:
            parsed = parse_row(row)
            rows.append(parsed)

        result = find_valid_numbers(rows)

        self.assertEqual(
            result, [467, 35, 633, 617, 592, 755, 664, 598, 97, 43, 98, 44, 1, 1, 56, 1]
        )

    def test_number_symbol_end(self):
        row14 = parse_row(matrix[14])
        row15 = parse_row(matrix[15])

        result = find_valid_numbers([row14, row15])

        self.assertEqual(result, [1, 1, 56])
