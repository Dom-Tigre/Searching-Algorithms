"""
This module contains tests for the searching algorithms learnt in the A-Level CS course
"""

import unittest
from searching import Search


class TestSearching(Search, unittest.TestCase):
    """
    This class contains unit tests for the searching algorithms
    """

    def test_binary_search(self):
        """
        This function tests the binary search algorithm
        """

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        floor = 0
        ceiling = len(arr) - 1
        target = 3
        result = self.binary_search(arr, floor, ceiling, target)
        expected_result = 2
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
