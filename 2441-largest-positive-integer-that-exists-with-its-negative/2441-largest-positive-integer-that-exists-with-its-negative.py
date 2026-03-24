class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans=[]
        for i in range(len(nums)):
            if nums[i] and -nums[i] in nums:
                ans.append(nums[i])
                ans.append(-nums[i])
        if not ans:
            return -1
        return max(ans)

        