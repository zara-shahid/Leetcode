class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=""
        while columnNumber>0:
            reminder=(columnNumber-1)%26
            char=chr(reminder+ord('A'))
            result=char+result
            columnNumber=(columnNumber-1)//26
        return result

        