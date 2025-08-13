class Solution:
    def __init__(self):
        self.memo={}
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        if n in self.memo:
            return self.memo[n]
        else:
            value=self.climbStairs(n - 1) + self.climbStairs(n - 2)
            self.memo[n]=value
        return value