class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        answer = 0
        mask = 0
        for right in range(len(nums)):
            while mask & nums[right] != 0:
                mask^=nums[left]
                left+=1
            mask|=nums[right]
            window=right-left+1
            answer=max(answer,window)
        return answer