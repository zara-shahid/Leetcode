class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        ans=""
        ans=" ".join(words[::-1])          
        return ans



        