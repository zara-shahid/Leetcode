class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        count1,count0=0,0
        max1,max0=0,0
        for i in range(len(s)):
            if s[i]=='1':
                count1+=1
                count0=0
            else:
                count0+=1
                count1=0
            max1=max(max1,count1)
            max0=max(max0,count0)   
        return max1>max0
        