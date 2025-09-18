from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count=Counter(arr)
        unique=0
        for word in arr:
            if count[word] == 1:
                unique += 1
                if unique == k:
                    return word
        return ""

            


        