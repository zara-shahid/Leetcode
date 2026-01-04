class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=sum(nums)
        op=0
        if s%k==0:
            return 0
        while s%k!=0:
            s-=1
            op+=1
        return op

        