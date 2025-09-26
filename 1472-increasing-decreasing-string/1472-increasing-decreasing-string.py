from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        count=Counter(s)
        result=""
        while len(result)<len(s):
            for i in "abcdefghijklmnopqrstuvwxyz":
                if count[i]>0:
                    result+=i
                    count[i]-=1
            for v in "zyxwvutsrqponmlkjihgfedcba":
                if count[v]>0:
                    result+=v
                    count[v]-=1
        return result
        