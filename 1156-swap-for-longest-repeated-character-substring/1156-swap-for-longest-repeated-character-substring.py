class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        answer = 0
        for target in count:
            left = 0 
            diff = 0
            for right in range(len(text)):
                if text[right]!=target:
                    diff+=1
                    while diff>1:
                        if text[left]!=target:
                            diff-=1
                        left+=1
                window_length = right - left + 1
                answer = max(answer, min(window_length, count[target]))
        return answer