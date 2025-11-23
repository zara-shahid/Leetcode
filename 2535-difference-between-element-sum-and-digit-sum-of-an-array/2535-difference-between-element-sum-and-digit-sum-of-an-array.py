class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum=0
        digit_sum=0
        for i in range(len(nums)):
            el_sum+=nums[i]
        digits = []
        for num in nums:
            for d in str(num):
                digits.append(int(d))
        for i in range(len(digits)):
            digit_sum+=digits[i]
        return abs(el_sum-digit_sum)

        