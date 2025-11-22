class Solution:
    def reverseBits(self, n: int) -> int:
        binary=f"{n:032b}"
        rev_binary=binary[::-1]
        return int(rev_binary,2)
        