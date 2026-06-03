import unittest
from game.objects.Pythomon import Pythomon
from game.objects.attacks.Scratch import Scratch


class PythomonTestCase(unittest.TestCase):
    def test_has_empty_name_and_hp(self):
        p = Pythomon()
        self.assertEqual("", p.name)
        self.assertEqual(0, p.hp)

    def test_has_empty_attack_list(self):
        p = Pythomon()
        self.assertIsInstance(p.attacks, list)
        self.assertEqual(0, len(p.attacks))

    def test_can_add_attack(self):
        p = Pythomon()
        p.add_attack(Scratch())
        self.assertEqual(1, len(p.attacks))

    def test_max_four_attacks(self):
        p = Pythomon()
        p.add_attack(Scratch())
        p.add_attack(Scratch())
        p.add_attack(Scratch())
        p.add_attack(Scratch())
        p.add_attack(Scratch())
        self.assertEqual(4, len(p.attacks))

if __name__ == '__main__':
    unittest.main()
