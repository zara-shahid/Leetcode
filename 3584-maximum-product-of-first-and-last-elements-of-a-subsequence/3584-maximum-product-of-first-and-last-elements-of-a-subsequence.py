class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        n = len(nums)
        ans = float('-inf')
        maxStart = float('-inf')
        minStart = float('inf')

        for j in range(m - 1, n):
            idx = j - m + 1
            maxStart = max(maxStart, nums[idx])
            minStart = min(minStart, nums[idx])
            ans = max(
                ans,
                nums[j] * maxStart,
                nums[j] * minStart
            )
        return ans