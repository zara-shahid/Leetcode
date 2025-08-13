class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[[1]]
        if numRows==1:
            return triangle
        prev_row=[1]
        for k in range(numRows-1):
            new_row=[1]
            for j in range(1,len(prev_row)):
                middle=prev_row[j-1]+prev_row[j]
                new_row.append(middle)
            new_row.append(1)
            triangle.append(new_row)
            prev_row=new_row
        return triangle
        

            


        