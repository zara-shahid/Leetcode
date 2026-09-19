class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(len(nums)-1):
            left = sum(nums[0:i+1])
            right = sum(nums[i+1:len(nums)])

            if (left-right)%2==0:
                count+=1

        return count
