class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0 
        s=s.rstrip()       
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                break
            count+=1
        return count

            
            
        