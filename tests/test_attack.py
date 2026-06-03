import unittest
from game.objects.Attack import Attack

class AttackTestCase(unittest.TestCase):
    def test_has_name_and_dmg(self):
        a = Attack("Scratch", 5)
        self.assertEqual("Scratch", a.name)
        self.assertEqual(5, a.damage)


if __name__ == '__main__':
    unittest.main()
