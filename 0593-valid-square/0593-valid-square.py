class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        distances = []
        for i in range(4):
            for j in range(i+1, 4):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                distances.append(dx*dx + dy*dy)
        side=min(distances)
        diagonal=max(distances)
        if side>0 and diagonal==2*side:
            return True
        return False
                
            

        