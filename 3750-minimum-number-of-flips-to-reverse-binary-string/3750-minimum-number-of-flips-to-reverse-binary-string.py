class Solution:
    def minimumFlips(self, n: int) -> int:
        
        s = bin(n)[2:]
        reverse_s = s[::-1]     
        flips = 0  
        for i in range(len(s)):
            if s[i] != reverse_s[i]:
                flips += 1
        
        return flips