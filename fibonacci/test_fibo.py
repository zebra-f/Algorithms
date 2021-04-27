import unittest
import fibo


class TestFibo(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibo.fibonacci(1), 1)
        self.assertEqual(fibo.fibonacci(2), 1)
        self.assertEqual(fibo.fibonacci(3), 2)
        self.assertEqual(fibo.fibonacci(4), 3)
        self.assertEqual(fibo.fibonacci(5), 5)
        self.assertEqual(fibo.fibonacci(6), 8)
        self.assertEqual(fibo.fibonacci(7), 13)
        self.assertEqual(fibo.fibonacci(8), 21)
        self.assertEqual(fibo.fibonacci(50), 12586269025)
        self.assertEqual(fibo.fibonacci(100), 354224848179261915075)


if __name__ == '__main__':
    unittest.main()
