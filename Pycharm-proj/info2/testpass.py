import unittest
from practice import LenghtFilter, SpecialCharFilter, AndFilter


class PassTestCase(unittest.TestCase):
    def test_length_filter(self):
        lenght_filter = LenghtFilter(8)
        result = lenght_filter.validate("12345678")
        self.assertEqual([], result)

    def test_len_fil_if_pass_not_ok(self):
        lenght_filter = LenghtFilter(8)
        result = lenght_filter.validate("123")
        self.assertTrue(len(result) > 0)

    def test_spec_char_filter_notok(self):
        # Needs 4 special chars, only gets 0
        spec_char = SpecialCharFilter(4)
        result = spec_char.validate("abcdef")
        self.assertTrue(len(result) > 0)

    def test_spec_char_filter_if_ok(self):
        # Needs 4, but "*,." is only 3.
        # Note: This will correctly return an error!
        spec_char = SpecialCharFilter(4)
        result = spec_char.validate("*,.abcdef")
        self.assertTrue(len(result) > 0)

    def test_and_ifok(self):  # Fixed the name typo here
        filters = []
        filters.append(SpecialCharFilter(1))  # Require 1 spec char
        filters.append(LenghtFilter(8))  # Require 8 chars

        and_filter = AndFilter(filters)
        # "abcde.,dfgh" has 11 chars and 2 spec chars. Should pass!
        result = and_filter.validate("abcde.,dfgh")

        self.assertEqual(len(result), 0, f"Expected no errors, but got: {result}")


if __name__ == '__main__':
    unittest.main()