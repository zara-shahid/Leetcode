class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0  
        prev2 = 0  

        for money in nums:
            prev2, prev1 = prev1, max(prev2 + money, prev1)

        return prev1
