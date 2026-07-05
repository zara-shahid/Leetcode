class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        r = len(nums) - 1
        op = 0

        for l in range(len(nums)):

            while l < r and nums[r] == 0:
                r -= 1

            if l < r and nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                op += 1
                r -= 1

        return op