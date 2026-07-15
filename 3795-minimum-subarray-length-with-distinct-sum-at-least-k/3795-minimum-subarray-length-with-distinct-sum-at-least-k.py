class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        left = 0
        distinct_sum = 0
        freq = {}
        ans = float('inf')

        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right], 0) +1
            if freq[nums[right]]==1:

                distinct_sum += nums[right]

            while distinct_sum >= k:
                ans = min(ans, right - left +1)
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    distinct_sum-=nums[left]
                left+=1

        if ans==float('inf'):
            return -1
        else:
            return ans

