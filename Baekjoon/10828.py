# 맞았습니다

import sys

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size()==0

    def top(self):
        if self.is_empty():
            return -1
        else:
            return self.stack[-1]


r = lambda : sys.stdin.readline()
n = r()

stack = Stack()
dict = {'top':stack.top(), 'size':stack.size(), 'empty':stack.is_empty(), 'pop':stack.pop()}
for _ in range(int(n)):
    input = str(r())
    if ' ' in input:
        a, b = input.split()
        stack.push(int(b))
    else:
        a = str(input.strip())
        if a == 'top':
            res = stack.top()
        elif a == 'size':
            res = stack.size()
        elif a == 'empty':
            res = stack.is_empty()
        elif a == 'pop':
            res = stack.pop()
        print(res)

    # print(stack.stack)
