from unittest import TestCase
from median import calculate_median


class TestCalculateMedian(TestCase):
    def test_median_list_even(self):
        my_numbers = [5,6,4,3]
        median_result = calculate_median(my_numbers)
        self.assertEqual(median_result, 4.5)

    def test_median_list_odd(self):
        my_numbers = [78, 67, 89, 65, 23]
        median_result = calculate_median(my_numbers)
        self.assertEqual(median_result,67)

    def test_median_list_one_element(self):
        my_numbers = [24]
        median_result = calculate_median(my_numbers)
        self.assertEqual( median_result, 24)

    def test_median_list_empty(self):
        my_numbers = []
        median_result = calculate_median(my_numbers)
        self.assertEqual(median_result, None)

