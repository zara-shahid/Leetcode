from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False
        
        i = 0
        
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        if i == 0 or i == n - 1:
            return False
        
        dec_start = i
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1
        
        if i == dec_start or i == n - 1:
            return False
        
        inc2_start = i
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        if i == n - 1 and inc2_start != i:
            return True
        
        return False
