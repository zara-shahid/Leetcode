class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        total = sum(nums)
        left = 0
        ans = 0

        for x in nums:
            if x == 0:
                right = total - left

                if left == right:
                    ans += 2
                elif abs(left - right) == 1:
                    ans += 1
            left += x
        return ans