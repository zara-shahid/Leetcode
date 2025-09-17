from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1=s1.split()
        w2=s2.split()
        c1=Counter(w1)
        c2=Counter(w2) 
        ans=[]
        for w,fr in c1.items():
            if w not in c2 and fr==1:
                ans.append(w)
        for z,fer in c2.items():
            if z not in c1 and fer==1:
                ans.append(z)
        return ans
               
