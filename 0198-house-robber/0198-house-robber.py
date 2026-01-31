class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        prev1=0
        prev2=0
        for i in range(0,len(nums)):
            curr=max(prev2+nums[i],prev1)
            prev2=prev1
            prev1=curr
        return curr
        