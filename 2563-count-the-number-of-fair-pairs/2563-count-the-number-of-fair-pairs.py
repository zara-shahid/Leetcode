class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        
        def count(target):
            left = 0
            right = len(nums) - 1
            pairs = 0
            
            while left < right:
                if nums[left] + nums[right] <= target:
                    pairs += right - left
                    left += 1
                else:
                    right -= 1
            
            return pairs
        
        return count(upper) - count(lower - 1)