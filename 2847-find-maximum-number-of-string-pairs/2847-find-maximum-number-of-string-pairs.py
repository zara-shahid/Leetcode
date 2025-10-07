from collections import Counter
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        sorted_words = [''.join(sorted(word)) for word in words]
        count=Counter(sorted_words)
        ans=0
        for i in count.values():
            if i==2:
                ans+=1
        return ans


        