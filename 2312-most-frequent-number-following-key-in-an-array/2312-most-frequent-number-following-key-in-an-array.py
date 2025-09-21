from collections import Counter
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count=Counter()
        for i in range(len(nums)-1):
            if nums[i]==key:
                count[nums[i+1]]+=1
        return max(count,key=count.get)
