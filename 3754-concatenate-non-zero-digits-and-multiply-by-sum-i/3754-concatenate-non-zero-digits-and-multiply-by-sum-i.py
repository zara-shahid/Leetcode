class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""
        summ=0
        for i in str(n):
            if i!="0":
                x+=i
        if x=="":
            return 0
        for s in x:
            summ+=int(s)
        return int(x)*summ
                
        