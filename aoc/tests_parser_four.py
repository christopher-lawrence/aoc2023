from django.test import TestCase

from .services.parser_four import Card

cards = [
    "Card   1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card   2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card   3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card   4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card   5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card   6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


class TestParserFour(TestCase):
    def test_card(self):
        card = Card("Card 1: 1 2 3 | 3 4 5", {})

        self.assertEqual(card.winners, [1, 2, 3])
        self.assertEqual(card.numbers, [3, 4, 5])

    def test_card_get_value(self):
        card = Card("Card 1: 1 2 3 | 3 4 5", {})

        self.assertEqual(card.winners, [1, 2, 3])
        self.assertEqual(card.numbers, [3, 4, 5])
        self.assertEqual(card.get_value(), 1)

    def test_card_get_value_multiple(self):
        card = Card("Card 1: 1 2 3 | 1 2 3", {})

        self.assertEqual(card.get_value(), 4)

    def test_card_with_spaces(self):
        card = Card(cards[0], {})

        self.assertEqual(card.winners, [41, 48, 83, 86, 17])
        self.assertEqual(card.numbers, [83, 86, 6, 31, 17, 9, 48, 53])

    def test_card_additional_cards(self):
        card_dict = {}
        card = Card(cards[0], card_dict)

        card.get_value()

        self.assertEqual(card.name, 1)
        self.assertEqual(card_dict, {2: 1, 3: 1, 4: 1, 5: 1})
