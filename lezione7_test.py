import unittest
from lezione7.py import somma

class TestSomma(unitetest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(1,1),2)
        self.assertEqual(somma(1.5,2.5),4)
        