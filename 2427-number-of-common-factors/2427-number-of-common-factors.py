class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        newa=str(a)
        newb=str(b)
        i=1
        count=0
        while i<=max(a,b):
            if a%i==0 and b%i==0:
                count+=1
            i+=1
        return count




        