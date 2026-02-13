from collections import Counter

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = max(count.values())
        
        first = {}
        last = {}
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
        
        min_length = float('inf')
        
        for num in count:
            if count[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)
        
        return min_length
