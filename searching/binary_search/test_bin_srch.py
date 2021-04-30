import unittest
import bin_srch


class TestBinSrch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(bin_srch.binary_search([], 2), None)
        self.assertEqual(bin_srch.binary_search([1], 2), None)
        self.assertEqual(bin_srch.binary_search([-1, 0, 1], 2), None)
        self.assertEqual(bin_srch.binary_search([-1, 0, 1], 2), None)

        self.assertEqual(bin_srch.binary_search([1], 1), 0)
        self.assertEqual(bin_srch.binary_search([-1, 0, 1], 1), 2)
        self.assertEqual(bin_srch.binary_search([-1, 0, 1, 2, 3, 4], 2), 3)

        self.assertEqual(bin_srch.binary_search([x for x in range(99)], 49), 49)


if __name__ == '__main__':
    unittest.main()
