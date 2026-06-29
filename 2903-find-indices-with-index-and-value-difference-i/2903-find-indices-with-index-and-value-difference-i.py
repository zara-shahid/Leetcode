class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    ans.append(i)
                    ans.append(j)
        if len(ans)==0:
            return [-1,-1]
        return ans
        