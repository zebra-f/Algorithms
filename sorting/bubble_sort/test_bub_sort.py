import unittest
import bub_sort


class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bub_sort.bubble_sort([]), [])
        self.assertEqual(bub_sort.bubble_sort([1]), [1])
        self.assertEqual(bub_sort.bubble_sort([2, 1]), [1, 2])
        self.assertEqual(bub_sort.bubble_sort([1, -1]), [-1, 1])
        self.assertEqual(bub_sort.bubble_sort([0, -1]), [-1, 0])
        self.assertEqual(bub_sort.bubble_sort([0, -1.5]), [-1.5, 0])
        self.assertEqual(bub_sort.bubble_sort([0.2, -1]), [-1, 0.2])
        self.assertEqual(bub_sort.bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(bub_sort.bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(bub_sort.bubble_sort([1, 2, 3.8, 4]), [1, 2, 3.8, 4])
        self.assertEqual(bub_sort.bubble_sort([7, 5, 3, -4, 2]), [-4, 2, 3, 5, 7])


if __name__ == '__main__':
    unittest.main()
