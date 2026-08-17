class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        s_arr = []
        ans = 0
        for i in range(len(nums)):
            current_sum = 0

            for j in range(i, len(nums)):
                current_sum += nums[j]
                s_arr.append(current_sum)

        s_arr = sorted(s_arr)
        ans = sum(s_arr[left-1:right])
        return ans % (10**9 + 7)


