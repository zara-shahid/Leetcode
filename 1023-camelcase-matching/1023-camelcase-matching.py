class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans=[]
        for query in queries:
            i=0
            j=0
            valid=True
            while i<len(query):
                if j<len(pattern) and query[i]==pattern[j]:
                    i+=1
                    j+=1
                else:
                    if query[i].islower():
                        i+=1
                    else:
                        if query[i].isupper():
                            valid=False
                        break
            if j!=len(pattern):
                valid=False
            
            ans.append(valid)
        return ans




 