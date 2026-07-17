class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        ans = 0
        freq = {}
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) +1
            window_sum+=nums[right]
            while freq[nums[right]] > 1:
                freq[nums[left]]-=1
                window_sum-=nums[left]
                left+=1
            ans = max(ans, window_sum)
        return ans