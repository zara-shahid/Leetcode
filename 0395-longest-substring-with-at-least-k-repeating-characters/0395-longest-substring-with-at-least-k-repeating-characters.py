class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        c=Counter(s)
        ans=0
        parts=[]
        for key, value in c.items():
            if value<k:
                parts=s.split(key)
                return max(
                    self.longestSubstring(part, k)
                    for part in parts)
        return len(s)