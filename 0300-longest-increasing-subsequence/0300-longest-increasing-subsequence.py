class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=len(nums)*[1]
        for j in range(len(nums)):
            for i in range(j):
                if nums[j]>nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
                

        