class Solution:
    def findLUSlength(self, strs: List[str]) -> int:

        def isSubsequence(s: str, t: str) -> bool:
            i = 0
            j = 0

            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1

            return i == len(s)

        ans = -1

        for i in range(len(strs)):
            is_uncommon = True

            for j in range(len(strs)):
                if i == j:
                    continue

                if isSubsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break

            if is_uncommon:
                ans = max(ans, len(strs[i]))

        return ans