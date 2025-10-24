class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count=Counter(nums)
        for fr in count.values():
            if fr%2!=0:
                return False
        return True

        