class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg=sum(nums)/len(nums)
        x = max(1, floor(avg) + 1)
        while True:
            if x not in nums:
                return x
            else:
                x += 1
        return max(nums)+1
        