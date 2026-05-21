class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)

        # Step 1: Build prefix sum array
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = float('inf')

        for start in range(n):

            for length in range(l, r + 1):

                end = start + length - 1

                if end >= n:
                    break

                current_sum = prefix[end + 1] - prefix[start]

                if current_sum > 0:
                    ans = min(ans, current_sum)

        if ans == float('inf'):
            return -1

        return ans