#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE        : PyCharm
@Author     : Panda
@Date       : 2023/10/4 12:00
@Description: 
"""


class Solution(object):
    """
    常规做法
    """


# def sortedSquares(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     nums = sorted([item * item for item in nums])
#     return nums


"""
双指针从两边向中间缩进，哪边绝对值大加入哪边的数
"""


def sortedSquares(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    left = 0
    right = len(nums) - 1
    res = [0]*len(nums)
    pos = len(nums)-1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res[pos] = nums[left] ** 2
            left += 1
        else:
            res[pos] = nums[right] ** 2
            right -= 1
        pos-=1
    return res
