class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        col1=ord(coordinate1[0])-ord('a')+1
        row1=int(coordinate1[1])
        col2=ord(coordinate2[0])-ord('a')+1
        row2=int(coordinate2[1])
        if ((row1+col1)%2==1)==((row2+col2)%2!=1):
            return False
        return True
        
        