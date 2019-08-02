#!/usr/bin/env python

# For a given chemical formula represented by a string, count the number of atoms of each element contained in the
# molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).
#
# For example:
#
#   water = 'H2O'
#    parse_molecule(water)                 # return {H: 2, O: 1}
#
#   magnesium_hydroxide = 'Mg(OH)2'
#   parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}
#
#   var fremy_salt = 'K4[ON(SO3)2]2'
#   parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}

# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to
# multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom,
# two nitrogen atoms and six oxygen atoms.
#
# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

import unittest

def parse_molecule (formula):
    pass


class TestParseMolecule(unittest.TestCase):

    def equals_atomically(self, obj1, obj2):
        if len(obj1) != len(obj2):
            return False
        for k in obj1:
            if obj1[k] != obj2[k]:
                return False
        return True

    def test_parse_molecule(self):
        self.assertEqual(self.equals_atomically(parse_molecule("H2O"), {'H': 2, 'O' : 1}), "Should parse water")
        self.assertEqual(self.equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
        self.assertEqual(self.equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")


if __name__ == '__main__':
    unittest.main()
