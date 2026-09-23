class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        t_sum = sum(nums)
        l_sum = 0

        for i in range(len(nums)):
            r_sum = t_sum - l_sum - nums[i]

            if l_sum == r_sum:
                return i

            l_sum += nums[i]

        return -1