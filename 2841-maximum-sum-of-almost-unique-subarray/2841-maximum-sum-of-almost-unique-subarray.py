from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        left = 0
        window_sum = 0
        ans = 0
        freq = {}

        for right in range(len(nums)):
            window_sum += nums[right]

            freq[nums[right]] = freq.get(nums[right], 0) + 1
            if right - left + 1 > k:
                window_sum -= nums[left]
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            if right - left + 1 == k:
                if len(freq) >= m:
                    ans = max(ans, window_sum)

        return ans