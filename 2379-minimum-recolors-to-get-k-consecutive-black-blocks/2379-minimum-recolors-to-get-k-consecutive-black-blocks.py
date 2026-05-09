class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        
        for i in range(len(blocks) - k + 1):
            s = blocks[i:i+k]
            
            count = 0
            
            for c in s:
                if c == "W":
                    count += 1
            
            ans = min(ans, count)
        
        return ans