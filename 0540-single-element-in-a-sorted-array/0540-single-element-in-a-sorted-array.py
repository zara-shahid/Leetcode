class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=Counter(nums)
        for key,value in n.items():
            if value==1:
                return key
            