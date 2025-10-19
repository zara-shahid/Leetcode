
from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        count=Counter(s)
        even_c=[]
        odd_c=[]
        for c in count.values():
            if c%2==0:
                even_c.append(c)
            else:
                odd_c.append(c)
        return max(odd_c)-min(even_c)
