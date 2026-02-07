class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        c=Counter(nums)
        n=set()
        for i in range(len(nums)-1):
            curr_sum=nums[i]+nums[i+1]
            if curr_sum in n:
                return True
            n.add(curr_sum)
        return False
