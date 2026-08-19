class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        ans = 0

        for i in range(n - 2):

            left_sum = prefix[i]

            left = bisect_left(
                prefix,
                2 * prefix[i],
                i + 1,
                n - 1
            )

            right = bisect_right(
                prefix,
                (prefix[-1] + prefix[i]) // 2,
                i + 1,
                n - 1
            ) - 1

            if left <= right:
                ans += right - left + 1

        return ans % (10**9 + 7)