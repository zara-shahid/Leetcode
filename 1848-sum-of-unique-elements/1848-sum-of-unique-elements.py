from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts=Counter(nums)
        ans=0
        for el,fr in counts.items():
            if fr==1:
                ans+=el
        return ans
        