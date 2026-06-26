class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        i=0
        j=len(nums)//2
        while i<(len(nums)//2) and j<len(nums):
            if 2*nums[i]<=nums[j]:
                i+=1
                j+=1
                count+=2
            else:
                j+=1
        return count

        