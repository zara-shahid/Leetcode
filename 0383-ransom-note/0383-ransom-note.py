class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans={}
        count=0
        for i in range(0,len(magazine)):
            if magazine[i] in ans:
                ans[magazine[i]]+=1
            else:
                ans[magazine[i]]=1
        for ch in range(0,len(ransomNote)):
            if ransomNote[ch] in ans and ans[ransomNote[ch]]>0:
                ans[ransomNote[ch]]-=1
            else:
                return False
        return True



            

        