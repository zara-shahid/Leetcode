class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=Counter(nums)
        max_len=0
        for val in n:
            if val+1 in n:
                max_len=max(max_len,n[val]+n[val+1])
        return max_len

        