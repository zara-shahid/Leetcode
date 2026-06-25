class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i<j<k:
                        triplet= (nums[i]-nums[j])*nums[k]
                        ans=max(triplet,ans)
        if ans>0:
            return ans
        return 0