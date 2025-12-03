class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        i=1
        count=0
        limit = min(a, b)
        while i<=limit:
            if a%i==0 and b%i==0:
                count+=1
            i+=1
        return count




        