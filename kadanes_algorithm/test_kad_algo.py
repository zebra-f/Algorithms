import unittest
import kad_algo


class TestKadAlgo(unittest.TestCase):

    def test_kadane_algo(self):
        self.assertEqual(kad_algo.kadane_algo([]), 0)
        self.assertEqual(kad_algo.kadane_algo([17]), 17)
        self.assertEqual(kad_algo.kadane_algo([17.2]), 17.2)
        self.assertEqual(kad_algo.kadane_algo([-17]), -17)
        self.assertEqual(kad_algo.kadane_algo([-17.2]), -17.2)
        self.assertEqual(kad_algo.kadane_algo([1, 1, 1, 1]), 4)
        self.assertEqual(kad_algo.kadane_algo([-2, 0, -1]), 0)
        self.assertEqual(kad_algo.kadane_algo([-2, -1, -3]), -1)
        self.assertEqual(kad_algo.kadane_algo([2, 2, 0]), 4)
        self.assertEqual(kad_algo.kadane_algo([-17, -2, -1]), -1)
        self.assertEqual(kad_algo.kadane_algo([13, -2, 11]), 22)
        self.assertEqual(kad_algo.kadane_algo([13, -2]), 13)
        self.assertEqual(kad_algo.kadane_algo([-1, 3, 6, 7, -9]), 16)
        self.assertEqual(kad_algo.kadane_algo([-1, 3, 6, 7.2, -9]), 16.2)
        self.assertEqual(kad_algo.kadane_algo([-1, 3, -2, 6, 7.2, -9]), 14.2)


if __name__ == '__main__':
    unittest.main()
