class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]<target and i<j:
                    pairs+=1
        return pairs
        