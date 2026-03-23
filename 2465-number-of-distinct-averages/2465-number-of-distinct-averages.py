class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        n=sorted(nums)
        ans=set()
        while len(n)>1:
            minimum=n.pop()
            maximum=n.pop(0)
            avg=(minimum+maximum)/2
            ans.add(avg)
        return len(ans)


        