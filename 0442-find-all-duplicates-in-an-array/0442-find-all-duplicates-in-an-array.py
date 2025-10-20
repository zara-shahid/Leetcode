from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        ans=[]
        for el,fr in count.items():
            if fr>1:
                ans.append(el)
        return ans
        