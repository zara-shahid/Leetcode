class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeat = -1

        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                if val in seen:
                    repeat = val
                else:
                    seen.add(val)

        missing = -1
        for num in range(1, n*n + 1):
            if num not in seen:
                missing = num
                break

        return [repeat, missing]
