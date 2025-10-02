from collections import Counter

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        digit = str(n)  
        dig_count = Counter(digit)  
        min_freq = min(dig_count.values())  
        candidates = [int(d) for d, freq in dig_count.items() if freq == min_freq]  
        return min(candidates)
