class Solution:
    def reverseByType(self, s: str) -> str:        
        letters = []
        special = []

        for ch in s:
            if ch.islower():
                letters.append(ch)
            else:
                special.append(ch)

        letters.reverse()
        special.reverse()

        result = []
        l = 0
        sp = 0

        for ch in s:
            if ch.islower():
                result.append(letters[l])
                l += 1
            else:
                result.append(special[sp])
                sp += 1

        return "".join(result)

        