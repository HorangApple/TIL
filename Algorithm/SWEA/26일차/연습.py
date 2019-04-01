import sys
sys.stdin = open('input.txt','r')

class Stack:
    def __init__(self, size = 100, data = None):
        self.top = -1
        self.size = size
        self.data = [""]*size

        if data != None:
            self.push(data)

    def push(self,data):
        self.top += 1
        if self.size < self.top:
            return -1
        else :
            self.data[self.top]=data
        
    def pop(self):
        if self.top<-1:
            return -1
        else:
            value = self.data[self.top]
            self.data[self.top]=""
            self.top-=1
            return value
    def all(self):
        print(self.data)

stack=Stack(10,1)
stack.push(10)
stack.push(11)
stack.push(10)
stack.push(11)
stack.push(10)
stack.push(11)
stack.all()
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.all()
