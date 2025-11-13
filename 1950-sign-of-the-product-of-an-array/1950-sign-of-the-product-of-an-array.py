class Solution:
    def arraySign(self, nums: List[int]) -> int:
        def signFunc(x):
            res = 1
            for i in x:
                res *= i
            if res < 0:
                return -1
            elif res == 0:
                return 0
            else:
                return 1
        
        return signFunc(nums)
