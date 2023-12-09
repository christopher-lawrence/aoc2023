from django.test import TestCase

from .services.parser_three import Location, Row, get_lines, get_number_locations, get_symblol_locations, parse_row

matrix = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
    ".........9",
]

matrix_str = "\n".join(matrix)


class ParserThreeTestCase(TestCase):
    def test_get_lines(self):
        result = get_lines(matrix_str)

        self.assertEqual(result[0], matrix[0])
        self.assertEqual(len(result), 11)

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

        expected: list[Location] = [Location("*", 3, 3)]

        self.assertEqual(result, expected)

    def test_get_symbol_locations_mixed(self):
        result = get_symblol_locations(matrix[4])

        expected = [Location("*", 3, 3)]

        self.assertEqual(result, expected)

    def test_get_symbol_locations_many(self):
        result = get_symblol_locations(matrix[8])

        expected = [Location("$", 3, 3), Location("*", 5, 5)]

        self.assertEqual(result, expected)

    def test_parse_row(self):
        result = parse_row(matrix[0])

        expected = Row([Location(467, 0, 2), Location(114, 5,  7)], [])

        self.assertEqual(result, expected)

    def test_parse_row_mixed(self):
        result = parse_row(matrix[4])

        expected = Row([Location(617, 0, 2)], [Location("*", 3, 3)])

        self.assertEqual(result, expected)

