from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1=Counter(word1)
        c2=Counter(word2)
        for letter in "abcdefghijklmnopqrstuvwxyz":
            fr1=c1[letter]
            fr2=c2[letter]
            if abs(fr2-fr1)>3:
                return False
        return True


        