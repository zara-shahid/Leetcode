class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:

        def atMost(limit):
            if limit < 0:
                return 0

            left = 0
            ans = 0
            consonants = 0
            freq = defaultdict(int)
            last = {}

            for right in range(len(word)):
                ch = word[right]

                if ch in "aeiou":
                    freq[ch] += 1
                    last[ch] = right
                else:
                    consonants += 1

                while consonants > limit:
                    if word[left] in "aeiou":
                        freq[word[left]] -= 1
                        if freq[word[left]] == 0:
                            del freq[word[left]]
                    else:
                        consonants -= 1
                    left += 1

                if len(freq) == 5:
                    earliest = min(last.values())
                    if earliest >= left:
                        ans += earliest - left + 1

            return ans

        return atMost(k) - atMost(k - 1)