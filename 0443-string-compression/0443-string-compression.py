class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0
        n = len(chars)

        while i < n:
            start = i

            while i < n and chars[i] == chars[start]:
                i += 1

            count = i - start

            chars[write] = chars[start]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write