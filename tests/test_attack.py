import unittest
from game.objects.Attack import Attack

class AttackTestCase(unittest.TestCase):
    def test_has_empty_name_and_dmg(self):
        a = Attack()
        self.assertEqual("", a.name)
        self.assertEqual(0, a.damage)


if __name__ == '__main__':
    unittest.main()
