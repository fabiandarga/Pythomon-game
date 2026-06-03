import unittest
from game.objects.Pythomon import Pythomon

class PythomonTestCase(unittest.TestCase):
    def test_has_empty_name_and_hp(self):
        p = Pythomon()
        self.assertEqual("", p.name)
        self.assertEqual(0, p.hp)


if __name__ == '__main__':
    unittest.main()
