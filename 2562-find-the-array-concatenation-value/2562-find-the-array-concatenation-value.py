class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        total = 0
        
        while l <= r:
            if l == r:
                total += nums[l]
            else:
                total += int(str(nums[l]) + str(nums[r]))
            
            l += 1
            r -= 1
        
        return total