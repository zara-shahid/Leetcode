class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        ans=0
        for i in range(n):
            num = start + 2*i
            nums.append(num)
        for i in nums:
            ans^=i
        return ans
        