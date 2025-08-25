class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result=0
        for val in columnTitle:
            number=ord(val)-ord('A')+1
            result=result*26+number
        return result
        