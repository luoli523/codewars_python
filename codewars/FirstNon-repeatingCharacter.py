#!/usr/bin/env python

# Write a function named first_non_repeating_letter that takes a string input,
# and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't',
# since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character,
# but the function should return the correct case for the initial letter.
#
# For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

import unittest
import re


def first_non_repeating_letter(string):
    if string not in ("", None):
        for c in string:
            p = r"" + c
            if len(re.findall(p, string, flags=re.IGNORECASE)) == 1:
                return c

    return ""


def first_non_repeating_letter2(string):
    string_lower = string.lower()
    for i, c in enumerate(string):
        if string_lower.count(c.lower()) == 1:
            return string[i]
    return ""


class TestNonRepeatingLetter(unittest.TestCase):

    def test_first_non_repeating_letter_simple(self):
        self.assertEqual(first_non_repeating_letter('a'), 'a')
        self.assertEqual(first_non_repeating_letter('stress'), 't')
        self.assertEqual(first_non_repeating_letter('moonmen'), 'e')

    def test_first_non_repeating_letter_empty(self):
        self.assertEqual(first_non_repeating_letter(''), '')

    def test_first_non_repeating_letter_odd(self):
        self.assertEqual(first_non_repeating_letter('~><#~><'), '#')
        self.assertEqual(first_non_repeating_letter('hello world, eh?'), 'w')

    def test_first_non_repeating_letter_case(self):
        self.assertEqual(first_non_repeating_letter('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')

    def test_first_non_repeating_letter_simple2(self):
        self.assertEqual(first_non_repeating_letter2('a'), 'a')
        self.assertEqual(first_non_repeating_letter2('stress'), 't')
        self.assertEqual(first_non_repeating_letter2('moonmen'), 'e')

    def test_first_non_repeating_letter_empty2(self):
        self.assertEqual(first_non_repeating_letter2(''), '')

    def test_first_non_repeating_letter_odd2(self):
        self.assertEqual(first_non_repeating_letter2('~><#~><'), '#')
        self.assertEqual(first_non_repeating_letter2('hello world, eh?'), 'w')

    def test_first_non_repeating_letter_case2(self):
        self.assertEqual(first_non_repeating_letter2('sTreSS'), 'T')
        self.assertEqual(first_non_repeating_letter2('Go hang a salami, I\'m a lasagna hog!'), ',')


if __name__ == '__main__':
    unittest.main()
