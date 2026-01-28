class Solution:
    def minSteps(self, n: int) -> int:
        d=2
        ans=0
        while n>1:
            if n%d==0:
                ans+=d
                n=n//d
            else:
                d+=1
        return ans

        
        