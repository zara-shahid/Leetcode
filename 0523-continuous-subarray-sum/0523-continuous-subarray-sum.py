class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        d = {0: -1}
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            remainder = prefix_sum % k

            if remainder in d:
                length = i - d[remainder]

                if length >= 2:
                    return True
            else:
                d[remainder] = i

        return False