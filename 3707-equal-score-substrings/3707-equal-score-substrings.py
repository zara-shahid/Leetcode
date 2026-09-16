class Solution:
    def scoreBalance(self, s: str) -> bool:
        total_score = 0

        for char in s:
            total_score += ord(char) - ord('a') + 1

        left_score = 0

        for i in range(len(s) - 1):
            left_score += ord(s[i]) - ord('a') + 1

            right_score = total_score - left_score

            if left_score == right_score:
                return True

        return False