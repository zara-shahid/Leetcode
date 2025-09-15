class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split()
        count=0
        for w in words:
            if all(b not in w for b in brokenLetters):
                count+=1
        return count


        