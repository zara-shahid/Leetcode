
class Solution:
    def waysToMakeFair(self, nums: list[int]) -> int:
        total_e = sum(nums[::2])
        total_o = sum(nums[1::2])

        left_e = 0
        left_o = 0
        count = 0

        for i in range(len(nums)):
            right_e = total_e - left_e
            right_o = total_o - left_o

            if i % 2 == 0:
                right_e -= nums[i]
            else:
                right_o -= nums[i]

            new_e = left_e + right_o
            new_o = left_o + right_e

            if new_e == new_o:
                count += 1

            if i % 2 == 0:
                left_e += nums[i]
            else:
                left_o += nums[i]

        return count