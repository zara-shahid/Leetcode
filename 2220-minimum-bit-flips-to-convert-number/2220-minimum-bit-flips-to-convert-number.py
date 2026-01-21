class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        
        flips = bin(start ^ goal).count("1")
        return flips