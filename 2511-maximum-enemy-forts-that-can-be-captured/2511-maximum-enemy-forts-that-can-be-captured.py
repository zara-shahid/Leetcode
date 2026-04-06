class Solution:
    def captureForts(self, forts: List[int]) -> int:
        prev = None
        prev_index = -1
        max_capture = 0
        for i in range(len(forts)):
            if forts[i] == 1 or forts[i] == -1:
                if prev is not None:
                    if (prev == 1 and forts[i] == -1) or (prev == -1 and forts[i] == 1):
                        zeros = i - prev_index - 1
                        max_capture = max(max_capture, zeros)
                prev = forts[i]
                prev_index = i
        return max_capture