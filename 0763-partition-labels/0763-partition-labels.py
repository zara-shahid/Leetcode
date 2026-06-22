class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start=0
        end=0
        size=0
        ans=[]
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        for m in range(len(s)):
            end=max(end,last[s[m]])
            if m==end:
                size=end-start+1
                ans.append(size)
                start=m+1
        return ans



        
