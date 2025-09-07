from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count=Counter(s)
        tar_count=Counter(target)
        copies=min(s_count[c]//tar_count[c] for c in tar_count)
        return copies
        