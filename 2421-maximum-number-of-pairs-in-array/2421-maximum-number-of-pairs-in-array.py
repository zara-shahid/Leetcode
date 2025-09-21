from collections import Counter
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        pairs=0
        leftovers=0
        for fr in count.values():
            pairs+=fr//2
            leftovers+=fr%2
        return [pairs,leftovers]
