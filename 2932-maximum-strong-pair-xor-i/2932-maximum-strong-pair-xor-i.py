class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                x=nums[i]
                y=nums[j]
                if abs(x-y)<=min(x,y):
                    current = x^y
                ans=max(ans,current)
        return ans
