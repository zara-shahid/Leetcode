class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words=sentence.split()
        index=0
        for word in words:
            index+=1
            if word[0 : len(searchWord)] == searchWord:
                return index
        return -1
        