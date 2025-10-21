class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()

        for ch in word:
            if ch.islower():
                lower.add(ch)
            elif ch.isupper():
                upper.add(ch.lower())
        return len(lower & upper)
