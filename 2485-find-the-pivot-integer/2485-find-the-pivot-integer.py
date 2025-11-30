class Solution:
    def pivotInteger(self, n: int) -> int:
        value= n*(n + 1) / 2
        x = sqrt(value)
        if x == int(x):
            return int(x)
        return -1

        