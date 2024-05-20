"""
This module contains searching algorithms learnt in the A-Level CS course
"""


class Search:
    """
    This class currently contains binary search
    """

    def binary_search(self, arr, floor, ceiling, target):
        """
        This function searches an array using binary search, assuming the array is sorted
        """
        
        if ceiling >= floor:

            mid = (ceiling + floor) // 2

            if arr[mid] == target:
                return mid

            elif arr[mid] > target:
                return binary_search(arr, floor, mid - 1, target)

            else:
                return binary_search(arr, mid + 1, ceiling, target)

        else:
            return False
