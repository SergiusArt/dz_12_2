import unittest

from utils.arrs import get, my_slice

class TestCalc(unittest.TestCase):
    """
    Тестирование функций файла arrs
    """

    def test_get(self):
        """
        Тестирование функции get
        """

        self.assertEqual(get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(get([], 0, "test"), "test")
        self.assertEqual(get([1, 2, 3], -1, "test"), "test")

    def test_my_slice(self):
        """
        Тестирование функции my_slice
        """

        self.assertEqual(my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(my_slice([], 1), [])
        self.assertEqual(my_slice([1, 2, 3, 4], -2), [3, 4])
        self.assertEqual(my_slice([1, 2, 3, 4], -3, -1), [2, 3])
        self.assertEqual(my_slice([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(my_slice([1, 2, 3], -4), [1, 2, 3])

