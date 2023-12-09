from django.test import TestCase

from .services.parser import combine_numbers, get_number, get_numbers, map_numbers

class ParserTestCase(TestCase):

    def test_get_numbers_edges(self):
        result = get_numbers("1asdf2")

        self.assertListEqual(result, [1,2])

    def test_get_numbers_inner(self):
        result = get_numbers("a12b")
        self.assertListEqual(result, [1,2])

    def test_get_numbers_single(self):
        result = get_numbers("as1fd")

        self.assertListEqual(result, [1, 1])

    def test_get_numbers_mapped(self):
        result = get_numbers("one2gda3fourfivesixseveneightnine")

        self.assertEqual(result, [1,9])

    def test_combine_numbers_edges(self):
        result = combine_numbers([1,2,3])

        self.assertEqual(result, 13)

    def test_combine_numbers_single(self):
        result = combine_numbers([1])

        self.assertEqual(result, 11)

    def test_combine_numbers_empty(self):
        result = combine_numbers([])

        self.assertEqual(result, 0)

    def test_map_numbers_edges(self):
        result = map_numbers("oneasdftwo")

        self.assertEqual(result, "1asdf2")

    def test_map_numbers_single(self):
        result = map_numbers("asdfone1qer")

        self.assertEqual(result, "asdf11qer")

    def test_map_numbers_overlap(self):
        result = map_numbers("twone3")

        self.assertEqual(result, "2ne3")

    def test_get_number_first_word_edge(self):
        result = get_number("one2three")

        self.assertEqual(result, 1)

    def test_get_number_first_word_inner(self):
        result = get_number("asdtwo1")

        self.assertEqual(result, 2)

    def test_get_number_first_word_overlap(self):
        result = get_number("asdtwone3")

        self.assertEqual(result, 2)

    def test_get_number_first_int_edge(self):
        result = get_number("1two3")

        self.assertEqual(result, 1)

    def test_get_number_last_word_edge(self):
        result = get_number("one2three", True)

        self.assertEqual(result, 3)

    def test_get_number_last_word_inner(self):
        result = get_number("one2threeasdf", True)

        self.assertEqual(result, 3)

    def test_get_number_last_int_edge(self):
        result = get_number("one2three4", True)

        self.assertEqual(result, 4)

    def test_get_number_last_int_beginning_edge(self):
        result = get_number("1asdfasdf", True)

        self.assertEqual(result, 1)
