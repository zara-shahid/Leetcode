class MyStack:

    def __init__(self):
        self.MyStack=[]
        

    def push(self, x: int) -> None:
        self.MyStack.append(x)

    def pop(self) -> int:
        return self.MyStack.pop()

    def top(self) -> int:
        return self.MyStack[-1]

    def empty(self) -> bool:
        return len(self.MyStack)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()