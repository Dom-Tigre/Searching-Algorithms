"""
This module contains searching algorithms learnt in the A-Level CS course
"""


class Search:
    """
    This class currently contains binary search
    """

    def linear_search(self, arr, target):
        """
        This function searches an array using linear search
        """

        for i in range(len(arr)):
            if arr[i] == target:
                return i

        return False

    def binary_search(self, arr, floor, ceiling, target):
        """
        This function searches an array using binary search, assuming the array is sorted
        """

        if ceiling >= floor:

            mid = (ceiling + floor) // 2

            if arr[mid] == target:
                return mid

            if arr[mid] > target:
                return self.binary_search(arr, floor, mid - 1, target)

            return self.binary_search(arr, mid + 1, ceiling, target)

        return False
