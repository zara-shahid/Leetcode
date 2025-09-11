class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pos = {word: i for i, word in enumerate(list1)}
        min_sum, result = float('inf'), []
        for j, w in enumerate(list2):
            if w in pos:
                index_sum = pos[w] + j
                if index_sum < min_sum:
                    min_sum, result = index_sum, [w]
                elif index_sum == min_sum:
                    result.append(w)
        return result
