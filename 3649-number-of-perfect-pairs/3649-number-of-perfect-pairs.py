class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums = sorted(abs(x) for x in nums)

        ans = 0
        j = 0
        n = len(nums)

        for i in range(n):
            while j < n and nums[j] <= 2 * nums[i]:
                j += 1
            ans += j - i - 1

        return ans