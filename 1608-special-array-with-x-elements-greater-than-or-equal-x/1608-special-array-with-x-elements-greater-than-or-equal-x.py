class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x=0
        nums.sort()
        while x<=len(nums):
            count=0
            for y in range(len(nums)):
                if nums[y] >= x:
                    count+=1
            if count==x:
                return x
            x+=1
        return -1
            
