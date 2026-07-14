class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        ans = float('inf')
        for i in range(len(cards)):
            curr_card = cards[i]
            if curr_card in last_seen:
                prev_index = last_seen[curr_card]
                ans = min(ans,i - prev_index + 1)
            last_seen[curr_card] = i

        if ans == float('inf'):
            return -1
        else:
            return ans


        