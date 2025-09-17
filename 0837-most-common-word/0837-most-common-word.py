from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cleaned = re.sub(r'[^a-z]', ' ', paragraph.lower())
        words = cleaned.split()
        count = Counter(words)
        most_com=""
        max_freq=0
        for word, freq in count.items():
            if word not in banned and freq>max_freq :
                most_com = word      
                max_freq = freq 
        return most_com

            

        