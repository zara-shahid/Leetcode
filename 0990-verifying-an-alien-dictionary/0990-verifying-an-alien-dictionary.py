class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_map = {ch: i for i, ch in enumerate(order)}
        for i in range(0,len(words)-1):
            w1,w2=words[i],words[i+1]
            for j in range(min(len(w1),len(w2))):
                if w1[j]!=w2[j]:
                    if alien_map[w1[j]]>alien_map[w2[j]]:
                        return False
                    break
            else:
                if len(w1)>len(w2):
                    return False
        return True

