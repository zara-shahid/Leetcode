class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for d in nums:
            digits = list(map(int, str(d)))     
            mx = max(digits)                    
            encrypted = int(str(mx) * len(digits))  
            res += encrypted
        return res

        