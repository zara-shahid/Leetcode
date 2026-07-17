class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ['a', 'e', 'i', 'o', 'u']
        left = 0
        count = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in v:
                count += 1
            if right - left +1 >k:
                if s[left] in v:
                    count -= 1
                left += 1

            if right - left +1 ==k:
                ans = max(ans, count)
        return ans
