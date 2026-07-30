class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        left = 0
        answer = 0
        for right in range(len(nums)):
            while nums[right] > nums[left] * k:
                left+=1
            answer = max(answer, right-left+1)
        return len(nums)-answer

        