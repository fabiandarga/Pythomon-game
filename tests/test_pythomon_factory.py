import unittest

from game.factories.PythomonFactory import pythomon_factory
from game.objects.Pythomon import Pythomon


class PythomonFactoryTest(unittest.TestCase):
    def test_generates_some_pythomon(self):
        p = pythomon_factory.generate_random()
        self.assertIsInstance(p, Pythomon)