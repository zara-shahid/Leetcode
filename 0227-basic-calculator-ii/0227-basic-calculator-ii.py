class Solution:
    def calculate(self, s: str) -> int:
        ans=[]
        current_no=0
        operator='+'
        for i in s + "+":
            if i.isdigit():
                current_no=current_no*10+int(i)

            elif i in "+-*/":
                if operator=="+":
                    ans.append(current_no)
                elif operator=="-":
                    ans.append(-current_no)
                elif operator=="*":
                    ans.append(ans.pop() * current_no)
                elif operator=="/":
                    ans.append(int(ans.pop() / current_no))
                operator=i
                current_no=0
        return sum(ans)



        