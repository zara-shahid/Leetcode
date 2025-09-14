from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first = Counter(words[0])
        ans=[]
        for word in words[1:]:
            first &= Counter(word)
        for char, freq in first.items():
            ans.extend([char] * freq)
        return ans

        

        
