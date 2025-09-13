from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return (max(Counter(ch for ch in s if ch in "aeiou").values(), default=0) +
                max(Counter(ch for ch in s if ch.isalpha() and ch not in "aeiou").values(), default=0))
