class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:

        stack=[]
        for i in nums:
            if len(stack)==0:
                stack.append(i)
            else:
                if stack[-1]<=i:
                    stack.append(i)
        return len(stack)

        