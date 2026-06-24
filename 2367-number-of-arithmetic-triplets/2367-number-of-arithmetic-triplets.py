class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        ans = 0

        for i in nums:
            if i + diff in s and i + 2 * diff in s:
                ans += 1

        return ans