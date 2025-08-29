class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        answer=[0]*n
        stack=[]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                idx=stack.pop()
                answer[idx]=i-idx
            stack.append(i)
        return answer

        
