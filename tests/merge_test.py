import unittest
from pt.merge import merge


class MergeTest(unittest.TestCase):
    def test_right_value(self):
        self.assertEqual(merge(
            iter(xrange(0, 5, 1)),
            iter(xrange(0, 5, 1))
        ), [0, 0, 1, 1, 2, 2, 3, 3, 4, 4])

        self.assertEqual(merge(
            iter(xrange(0, 5, 5)),
            iter(xrange(0, 5, 1))
        ), [0, 0, 1, 2, 3, 4])

        self.assertEqual(merge(
            iter(reversed(range(0, 5, 1))),
        ), [4, 3, 2, 1, 0])

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            merge(None)

        with self.assertRaises(BaseException):
            merge()
