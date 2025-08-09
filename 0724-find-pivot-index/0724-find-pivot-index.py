class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        running_sum=0
        leftSum=0
        rightSum=0
        for i,val in enumerate(nums):
            leftSum=running_sum
            rightSum = total_sum - running_sum - nums[i]
            running_sum+=val
            if leftSum==rightSum:
                return i    
        return -1



            
        
        