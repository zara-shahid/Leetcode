class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict={}
        for i,val in enumerate(nums):
            complement=target-val
            if complement in dict:
                return dict[complement],i
            else:
                dict[val]=i


        