import statistics
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        median=int(statistics.median(nums))
        return sum(abs(x-median) for x in nums)
        