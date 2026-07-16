class Solution:
    def atMost(self, nums: List[int], k: int) -> int:
        left = 0
        freq = {}
        distinct = 0
        count = 0

        for right in range(len(nums)):
 
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if freq[nums[right]] == 1:
                distinct += 1

            while distinct > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    distinct -= 1

                left += 1
            count += right - left + 1

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)