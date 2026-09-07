class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        leftSum = 0
        rightSum = 0
        total = sum(nums)
        for i in range(len(nums)):
            rightSum = total - leftSum - nums[i]
            ans.append(abs(leftSum - rightSum))
            leftSum+=nums[i]
        return ans
        

        