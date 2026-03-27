class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        k-=1
        s = list(s)
        l = 0
        if k > len(s):
            return s
        else:
        
            while l < k:
                s[l], s[k] = s[k], s[l]
                l += 1
                k -= 1
            
            return "".join(s)