class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0]*len(nums)
        product = 1
        left = [0]*len(nums)
        right = [0]*len(nums)

        for i in range(len(nums)):
            left[i] = product
            product *= nums[i]

        product = 1
        
        for j in range(len(nums)-1,-1,-1):
            right[j] = product
            product *= nums[j]
        
        ans = [a * b for a, b in zip(left, right)]
        return ans

        