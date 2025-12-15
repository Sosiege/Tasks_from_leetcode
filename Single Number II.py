class Solution:
    def singleNumber(self, nums):
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 1:
            if nums[i] == nums[i + 1] == nums[i + 2]:
                i += 3
            else:
                return nums[i]
        return nums[-1]