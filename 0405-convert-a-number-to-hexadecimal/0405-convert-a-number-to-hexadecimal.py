class Solution:
    def toHex(self, num: int) -> str:
        return hex(num & 0xffffffff)[2:]
