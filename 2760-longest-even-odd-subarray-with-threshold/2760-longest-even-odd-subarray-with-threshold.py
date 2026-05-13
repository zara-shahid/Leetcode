class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        ans = 0
        current_len = 0

        for i in range(len(nums)):
            if nums[i] > threshold:
                current_len = 0

            elif nums[i] % 2 == 0:

                if i > 0 and current_len > 0 and nums[i-1] % 2 != nums[i] % 2:
                    current_len += 1

                else:
                    current_len = 1

            else:

                if i > 0 and current_len > 0 and nums[i-1] % 2 != nums[i] % 2:
                    current_len += 1

                else:
                    current_len = 0

            ans = max(ans, current_len)

        return ans