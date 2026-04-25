class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for w,word in enumerate(words):
            if x in word:
                ans.append(w)
        return ans