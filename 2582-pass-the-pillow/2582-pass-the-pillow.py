class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n - 1)
        t = time % cycle
        if t < n:
            return 1 + t
        else:
            return n - (t - (n - 1))

