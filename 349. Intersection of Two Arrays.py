"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

Runtime: 36 ms, faster than 99.34% of Python3 online submissions for Intersection of Two Arrays.
"""


def intersection(nums1, nums2):
    set_1 = set(nums1)
    set_2 = set(nums2)
    return list(set_1.intersection(set_2))
