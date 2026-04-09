class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        valid_words=set()
        best_word=""
        for word in words:
            if len(word)==1:
                valid_words.add(word)
                
            elif word[:-1] in valid_words:
                valid_words.add(word)

            if word in valid_words:
                if len(word)>len(best_word):
                        best_word=word
                elif len(word)==len(best_word):
                    if word<best_word:
                        best_word=word

        return best_word
            
        