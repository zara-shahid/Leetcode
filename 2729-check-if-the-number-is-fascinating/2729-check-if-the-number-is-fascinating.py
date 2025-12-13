class Solution:
    def isFascinating(self, n: int) -> bool:
        con=str(n)+str(2*n)+str(3*n)
        if len(con)!=9:
            return False
        return set(con)==set("123456789")
        