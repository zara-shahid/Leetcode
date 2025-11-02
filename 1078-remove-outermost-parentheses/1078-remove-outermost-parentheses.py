class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result=""
        count=0
        for c in s:
            if c=="(":
                if count>0:
                    result+="("
                count+=1
            else:
                count-=1
                if count>0:
                    result+=")"
        return result

        