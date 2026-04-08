class Solution:
    def longestPalindrome(self, s: str) -> str:
        r=len(s)-1
        longest=""
        for l in range(len(s)):
            for r in range(l,len(s)):
                portion=s[l:r+1]
                if portion==portion[::-1]:
                    if len(portion)>len(longest):
                        longest=portion

        return longest


        