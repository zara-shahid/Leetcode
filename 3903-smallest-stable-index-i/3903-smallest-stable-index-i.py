class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = []

        for i in range(len(nums)):
            left = nums[0:i+1]
            right = nums[i:n]

            if max(left)-min(right)<=k:
                ans.append(i)

        if len(ans)!=0:
            return min(ans)
        else:
            return -1
        