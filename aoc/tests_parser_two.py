from django.test import TestCase

from .services.parser_two import Game, parse_details, parse_game


class ParserTwoTestCase(TestCase):
    def test_parser_two_parse_details(self):
        detail = "1 Blue, 2 Red, 3 Green"

        result = parse_details(detail)

        self.assertEqual(result, (2, 3, 1))

    def test_parser_two_parse_game(self):
        game = "Game 1: 1 Red, 2 Green, 3 Blue"

        result = parse_game(game)

        expected = Game(1)
        expected.add_round(1, 2, 3)

        self.assertEqual(result, expected)

    def test_parser_two_parse_game_advanced(self):
        game = "Game 1: 1 Red, 2 Green, 3 Blue; 4 Red, 5 Green, 6 Blue"

        result = parse_game(game)

        expected = Game(1)
        expected.add_round(1, 2, 3)
        expected.add_round(4, 5, 6)

        self.assertEqual(result, expected)

    def test_parse_two_valid_game(self):
        game = Game(1)
        game.add_round(5, 5, 5)

        result = game.is_valid_game(4, 4, 4)

        self.assertEqual(result, True)
        self.assertEqual(game.id, 1)
