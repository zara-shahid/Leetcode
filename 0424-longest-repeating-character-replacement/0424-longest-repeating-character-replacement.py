class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq={}
        ans=0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            m_fr_ch=max(freq.values())
            
            if (r-l+1)-m_fr_ch>k:
                freq[s[l]]-=1
                l+=1
            ans=max(ans,r-l+1)
        return ans




        