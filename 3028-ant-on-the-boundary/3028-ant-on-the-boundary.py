class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        position = 0
        count = 0
        for i in range(len(nums)):
            position+=nums[i]
            if position == 0:
                count+=1
        return count