class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack=[]
        for i in nums:
            stack.append(i)
            while len(stack) >= 2 and stack[-2] > stack[-1]:
                a = stack.pop()
                b = stack.pop()
                stack.append(max(a, b))
        return len(stack)

        