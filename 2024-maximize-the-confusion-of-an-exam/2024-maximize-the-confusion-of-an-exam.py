class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answer=0
        for target in ["T", "F"]:
            left=0
            count=0
            for right in range(len(answerKey)):
                if answerKey[right]!=target:
                    count+=1
                while count>k:
                    if answerKey[left]!=target:
                        count-=1
                    left+=1
                window_length = right - left + 1
                answer = max(answer, window_length)
        return answer

        

        