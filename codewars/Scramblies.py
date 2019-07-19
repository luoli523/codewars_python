#!/usr/bin/env python

# Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged
# to match str2, otherwise returns false.
#
# Notes:
#
#   Only lower case letters will be used (a-z). No punctuation or digits will be included.
#   Performance needs to be considered
#
# Input strings s1 and s2 are null terminated.

# Examples
#   scramble('rkqodlw', 'world') ==> True
#   scramble('cedewaraaossoqqyt', 'codewars') ==> True
#   scramble('katas', 'steak') ==> False

import unittest


# inefficiently
def scramble(s1, s2):
    for c in s2:
        if s1.count(c) < 1:
            return False
    return True


def scramble2(s1, s2):
    s1_sort = ''.join(sorted(s1))
    s2_sort = ''.join(sorted(s2))

    if s1_sort == s2_sort:
        return True

    start_index = 0
    for c2 in s2_sort:
        for i in range(start_index, len(s1_sort)):
            start_index = i + 1
            if s1_sort[i] > c2:
                return False
            if s1_sort[i] == c2:
                break

    return True


class TestScramblies(unittest.TestCase):

    def test_scramble(self):
        self.assertEqual(scramble('rkqodlw', 'world'),  True)
        self.assertEqual(scramble('cedewaraaossoqqyt', 'codewars'), True)
        self.assertEqual(scramble('katas', 'steak'), False)
        self.assertEqual(scramble('scriptjava', 'javascript'), True)
        self.assertEqual(scramble('scriptingjava', 'javascript'), True)
        self.assertEqual(scramble('nrmljmfklkgvgyuupqu', 'mglunrkypuqjumlgkfv'), True)

    def test_scramble2(self):
        self.assertEqual(scramble2('rkqodlw', 'world'),  True)
        self.assertEqual(scramble2('cedewaraaossoqqyt', 'codewars'), True)
        self.assertEqual(scramble2('katas', 'steak'), False)
        self.assertEqual(scramble2('scriptjava', 'javascript'), True)
        self.assertEqual(scramble2('scriptingjava', 'javascript'), True)
        self.assertEqual(scramble2('nrmljmfklkgvgyuupqu', 'mglunrkypuqjumlgkfv'), True)


if __name__ == '__main__':
    unittest.main()
