class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        start = -1
        end = -1
        
        for i in range(len(nums)):
            if nums[i] != s_nums[i]:
                if start == -1:
                    start = i
                end = i
        
        if start == -1:   
            return 0
        
        return end - start + 1