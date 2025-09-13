from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels="aeiou"
        vowel=[]
        conso=[]
        ans=0
        max_vow,max_conso=0,0
        for ch in s:
            if ch in vowels:
                vowel.append(ch)
            else:
                conso.append(ch)
        c_vowel=Counter(vowel)
        c_conso=Counter(conso)
        for e,fr in c_vowel.items():
            if fr>max_vow:
                max_vow=fr
        for e, fr in c_conso.items():
            if fr > max_conso:
                max_conso = fr
        ans=max_vow+max_conso
        return ans
        

        
        
        