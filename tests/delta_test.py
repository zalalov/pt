import unittest
from pt.delta import to_seconds


class DeltaTest(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(to_seconds("s"), 1)
        self.assertEquals(to_seconds("1s"), 1)
        self.assertEquals(to_seconds("60 s"), 60)
        self.assertEquals(to_seconds("60"), 60)

        self.assertEqual(to_seconds("m"), 60)
        self.assertEquals(to_seconds("60m"), 3600)
        self.assertEquals(to_seconds("60 m"), 3600)

        self.assertEqual(to_seconds("h"), 3600)
        self.assertEquals(to_seconds("2h"), 7200)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            to_seconds(None)

        with self.assertRaises(ValueError):
            to_seconds("--")

        with self.assertRaises(ValueError):
            to_seconds(0)
