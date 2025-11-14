class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans=0
        while n>0:
            rem=n%k
            n=n//k
            ans+=rem
        return ans


        