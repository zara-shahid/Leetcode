from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count=Counter(chars)
        answer=0
        for word in words:
            good=True
            word_count=Counter(word)
            for c in word_count:
                if word_count[c]>char_count[c]:
                    good=False
                    break
            if good:
                answer+=len(word)
        return answer


        
               

        
        