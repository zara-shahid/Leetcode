class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        moves=0
        for i in nums:
            if i!=m:
                while i!=m:
                    moves+=1
                    i+=1
        return moves
        