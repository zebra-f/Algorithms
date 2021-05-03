import unittest
import bin_srch_r


class TestBinSrchR(unittest.TestCase):

    def test_binary_search_r(self):
        self.assertEqual(bin_srch_r.binary_search_r([], 2, starting_index=None, ending_index=None), None)
        self.assertEqual(bin_srch_r.binary_search_r([1], 2, starting_index=None, ending_index=None), None)
        self.assertEqual(bin_srch_r.binary_search_r([-1, 0, 1], 2, starting_index=None, ending_index=None), None)
        self.assertEqual(bin_srch_r.binary_search_r([-1, 0, 1], 2, starting_index=None, ending_index=None), None)

        self.assertEqual(bin_srch_r.binary_search_r([1], 1, starting_index=None, ending_index=None), 0)
        self.assertEqual(bin_srch_r.binary_search_r([-1, 0, 1], 1, starting_index=None, ending_index=None), 2)
        self.assertEqual(bin_srch_r.binary_search_r([-1, 0, 1, 2, 3, 4], 2, starting_index=None, ending_index=None), 3)

        self.assertEqual(bin_srch_r.binary_search_r(
            [x for x in range(99)], 49, starting_index=None, ending_index=None), 49)


if __name__ == '__main__':
    unittest.main()
