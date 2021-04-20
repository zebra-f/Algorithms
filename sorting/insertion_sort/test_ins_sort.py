import unittest
import ins_sort


class TestInsSort(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertEqual(ins_sort.insertion_sort([]), [])
        self.assertEqual(ins_sort.insertion_sort([1]), [1])
        self.assertEqual(ins_sort.insertion_sort([2, 1]), [1, 2])
        self.assertEqual(ins_sort.insertion_sort([1, -1]), [-1, 1])
        self.assertEqual(ins_sort.insertion_sort([0, -1]), [-1, 0])
        self.assertEqual(ins_sort.insertion_sort([0, -1.5]), [-1.5, 0])
        self.assertEqual(ins_sort.insertion_sort([0.2, -1]), [-1, 0.2])
        self.assertEqual(ins_sort.insertion_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(ins_sort.insertion_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(ins_sort.insertion_sort([1, 2, 3.8, 4]), [1, 2, 3.8, 4])
        self.assertEqual(ins_sort.insertion_sort([7, 5, 3, -4, 2]), [-4, 2, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()
