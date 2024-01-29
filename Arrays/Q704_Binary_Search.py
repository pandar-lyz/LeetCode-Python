class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # 防止溢出
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))
res = [[0] * 3] * 3
res[0][2] = 2

print(res)
print(3 // 2)
