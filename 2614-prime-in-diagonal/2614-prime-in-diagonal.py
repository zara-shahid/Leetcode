class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        ans = []
        n = len(nums)

        primary = [nums[i][i] for i in range(n)]
        secondary = [nums[i][n - 1 - i] for i in range(n)]

        res = list(set(primary + secondary))

        for x in res:
            if x < 2:
                continue

            is_prime = True
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    is_prime = False
                    break

            if is_prime:
                ans.append(x)

        return max(ans) if ans else 0
