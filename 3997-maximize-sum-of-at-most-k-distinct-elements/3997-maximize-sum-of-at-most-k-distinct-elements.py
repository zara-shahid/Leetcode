class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        rev = sorted(nums, reverse=True)
        ans=[]
        for i in rev:
            if i not in ans:
                ans.append(i)
                k-=1
            if k==0:
                break
        return ans

        