class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        pairs = 0
        freq = {}
        ans = 0
        for right in range(len(nums)):
            pairs += freq.get(nums[right], 0)
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            while pairs>=k:
                ans += len(nums)-right
                pairs -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left+=1
        return ans
