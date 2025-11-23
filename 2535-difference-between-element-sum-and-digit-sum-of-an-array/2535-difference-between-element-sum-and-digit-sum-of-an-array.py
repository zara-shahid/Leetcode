class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = sum(nums)
        digit_sum = sum(int(d) for num in nums for d in str(num))
        return abs(el_sum - digit_sum)
