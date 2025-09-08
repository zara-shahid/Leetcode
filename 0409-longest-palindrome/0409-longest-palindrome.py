from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        length=0
        odd_found=False
        s_count=Counter(s)
        for c in s_count:
            if s_count[c]%2==0:
                length+=s_count[c]
            else:
                length+=s_count[c]-1
                odd_found=True
        if odd_found:
            length+=1
        return length



        