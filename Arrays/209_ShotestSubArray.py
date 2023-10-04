#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE        : PyCharm
@Author     : Panda
@Date       : 2023/10/4 12:25
@Description: 
"""

if __name__ == "__main__":
    pass


def minSubArrayLen(self, target, nums):
    minLen = 1e6
    slowIndex = 0
    fastIndex = 0
    sumOfNum = 0
    # while fastIndex < len(nums):
    #     while (fastIndex < len(nums)) & (sumOfNum < target):
    #         sumOfNum += nums[fastIndex]
    #         fastIndex += 1
    #     while (slowIndex <= fastIndex) & (sumOfNum >= target):
    #         if (sumOfNum >= target) & (minLen > fastIndex - slowIndex):
    #             minLen = fastIndex - slowIndex
    #         sumOfNum -= nums[slowIndex]
    #         slowIndex += 1

    while fastIndex < len(nums):
        sumOfNum += nums[fastIndex]
        while sumOfNum >= target:
            minLen = min(minLen, fastIndex - slowIndex + 1)
            sumOfNum -= nums[slowIndex]
            slowIndex += 1
        fastIndex += 1

    if minLen == 1e6:
        return 0
    else:
        return minLen


"""
优化版本
"""
