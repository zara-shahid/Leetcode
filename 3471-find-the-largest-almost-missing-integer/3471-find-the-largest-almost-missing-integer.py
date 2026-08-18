class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}
        n = len(nums)

        for i in range(n - k + 1):
            subarray = nums[i:i+k]

            for x in set(subarray):
                freq[x] = freq.get(x, 0) + 1

        ans = -1

        for x in freq:
            if freq[x] == 1:
                ans = max(ans, x)

        return ans