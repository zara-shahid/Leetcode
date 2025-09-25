class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        al=set(allowed)
        count=0
        for i in words:
            if all(ch in al for ch in i):
                count+=1
        return count
                
        