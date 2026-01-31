class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        prev1 = 0   
        prev2 = 0 
        p1=0
        p2=0  

        for i in range(len(nums)-1):
            prev2, prev1 = prev1, max(prev2 + nums[i], prev1)
        for j in range(1,len(nums)):
            p2, p1 = p1, max(p2 + nums[j], p1)
        

        return max(prev1,p1)