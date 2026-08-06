class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        ans = 0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            required = ceil(prefix_sum/(i+1))
            ans = max(ans,required)
        return ans
        