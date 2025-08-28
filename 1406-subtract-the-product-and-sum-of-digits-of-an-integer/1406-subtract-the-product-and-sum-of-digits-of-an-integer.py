class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        addition=0
        while n>0:
            i=n%10
            n=n//10
            product*=i
            addition+=i
        return product-addition
        