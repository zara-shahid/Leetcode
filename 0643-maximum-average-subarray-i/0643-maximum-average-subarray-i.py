class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=0
        old_sum=sum(nums[:k])
        max_sum=old_sum
        for i in range(k,len(nums)):
            window_sum=old_sum-nums[i-k]+nums[i]
            old_sum=window_sum
            max_sum=max(window_sum,max_sum)
        return max_sum/k

        