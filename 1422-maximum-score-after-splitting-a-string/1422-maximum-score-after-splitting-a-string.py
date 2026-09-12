class Solution:
    def maxScore(self, s: str) -> int:
        zeros_left = 0
        ones_right = 0

        for i in s:
            if i == '1':
                ones_right += 1

        ans = 0

        for c in s[:-1]:
            if c == "0":
                zeros_left += 1
            else:
                ones_right -= 1

            score = zeros_left + ones_right
            ans = max(ans, score)

        return ans