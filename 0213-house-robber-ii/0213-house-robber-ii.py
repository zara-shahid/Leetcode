class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev1 = prev2 = 0
        for i in range(len(nums) - 1):
            prev2, prev1 = prev1, max(prev2 + nums[i], prev1)
        max1 = prev1

        prev1 = prev2 = 0
        for i in range(1, len(nums)):
            prev2, prev1 = prev1, max(prev2 + nums[i], prev1)
        max2 = prev1

        return max(max1, max2)
