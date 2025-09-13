from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        c_vowel = Counter(ch for ch in s if ch in vowels)
        c_conso = Counter(ch for ch in s if ch.isalpha() and ch not in vowels)
        return (max(c_vowel.values(), default=0) +
                max(c_conso.values(), default=0))
