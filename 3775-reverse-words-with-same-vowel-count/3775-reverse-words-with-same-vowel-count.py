class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = s.split()
        target = 0
        
        for ch in words[0]:
            if ch in vowels:
                target += 1

        for i in range(1, len(words)):
            count = 0

            for ch in words[i]:
                if ch in vowels:
                    count += 1

            if count == target:
                words[i] = words[i][::-1]

        return " ".join(words)