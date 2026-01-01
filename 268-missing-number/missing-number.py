class Solution(object):
    def missingNumber(self, nums):
        total=0
        for i in range(len(nums)):
            total+=nums[i]
        n = len(nums)
        return n * (n + 1) // 2 - total
        