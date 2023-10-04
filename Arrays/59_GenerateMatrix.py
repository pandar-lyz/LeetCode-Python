#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@IDE        : PyCharm
@Author     : Panda
@Date       : 2023/10/4 13:02
@Description: 
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        top = 0
        bott = n - 1
        left = 0
        right = n - 1

        k = 1
        while k <= n ** 2:
            for i in range(left, right + 1):
                matrix[top][i] = k
                k += 1
            top += 1
            for i in range(top, bott + 1):
                matrix[i][right] = k
                k += 1
            right -= 1
            for i in range(right, left - 1, -1):
                matrix[bott][i] = k
                k += 1
            bott -= 1
            for i in range(bott, top - 1, -1):
                matrix[i][left] = k
                k += 1
            left += 1
        return matrix

if __name__ == "__main__":
    pass
