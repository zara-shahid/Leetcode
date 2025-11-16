class Solution:
    def isThree(self, n: int) -> bool:
        root=int(n**0.5)
        if root*root!=n:
            return False
        p=root
        if p<2:
            return False
        for i in range(2,int(p**0.5)+1):
            if p % i == 0:
                return False
        return True
        
        