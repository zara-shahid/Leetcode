class Solution:
    def minElement(self, nums: List[int]) -> int:
        result=[]
        for i in nums:
            ans=0
            for d in str(i):
                ans+=int(d)
            result.append(ans)
        return min(result)
        