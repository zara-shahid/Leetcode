class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res=[-1]*len(nums)
        n = len(nums)
        stack=[]
        for i in range(2 * n - 1, -1, -1):  
            index = i % n  
            while stack and stack[-1]<=nums[index]:
                stack.pop()
            if not stack:
                res[index]=-1
            else:
                res[index]=stack[-1]
            stack.append(nums[index])
        return res


        