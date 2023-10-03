class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cur = 0
        idx = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[cur] = nums[idx]
                cur += 1
        return cur
