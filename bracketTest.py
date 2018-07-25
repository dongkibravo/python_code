
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size()==0


str = input("enter a question type input: ")

stack = Stack()
for c in str:
    if c=="(" or c=="{" or c=="[":
        stack.push(c)
    else:
        if c==")":
            if stack.pop()!="(":
                print("Error")
        elif c=="}":
            if stack.pop()!="{":
                print("Error")
        elif c=="]":
            if stack.pop()!="[":
                print("Error")

if stack.is_empty():
    print("No Error")
else:
    print("Error")
