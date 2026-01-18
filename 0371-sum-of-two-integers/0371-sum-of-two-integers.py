class Solution:
    def getSum(self, a: int, b: int) -> int:
        partial=a^b
        carry=(a & b) <<1
        return partial+carry
        