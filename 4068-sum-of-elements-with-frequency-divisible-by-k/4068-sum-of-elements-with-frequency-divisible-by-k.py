from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        ans=0
        for el,fr in count.items():
            if fr%k==0:
                ans+=el*fr
        return ans

        