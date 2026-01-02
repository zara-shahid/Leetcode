class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n==0:
            return False
        sum_dig=0
        prod_dig=1
        final=0
        for i in str(n):
            sum_dig+=int(i)
            prod_dig*=int(i)
        final=sum_dig+prod_dig
        if n%final==0:
            return True
        return False
        