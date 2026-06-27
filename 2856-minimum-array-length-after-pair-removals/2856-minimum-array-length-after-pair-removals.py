class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        count=0
        i=0
        j=len(nums)//2
        while i<(len(nums)//2) and j<len(nums):
            if nums[i]<nums[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return len(nums)-2*count