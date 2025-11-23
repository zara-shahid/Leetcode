class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans=0
        for i, digit in enumerate(nums):
            if i%2==0:
                ans+=digit
            else:
                ans-=digit
        return ans
        