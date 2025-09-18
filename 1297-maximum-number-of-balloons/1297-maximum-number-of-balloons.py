from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count=Counter(text)
        need = Counter("balloon")
        ratio=[]
        for ch in need:
            available=count[ch]
            req=need[ch]
            ratio.append(available//req)
        return min(ratio)

        