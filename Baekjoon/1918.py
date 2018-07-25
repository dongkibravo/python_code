# Right Answer

import sys

class Stack(object):
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
        return self.size() == 0

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]


def get_op_weight(op):
    if op  == '(':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2

r = lambda : sys.stdin.readline()
input = str(r().strip())
stack = Stack()
res = ''
for c in input:
    if c.isalpha():
        res += c
    else:
        if c == '(' or stack.is_empty():
            stack.push(c)
        elif c == ')':
            op = stack.pop()
            while op != '(':
                res += op
                op = stack.pop()
        elif get_op_weight(c)>get_op_weight(stack.top()):
            stack.push(c)
        else:
            while not stack.is_empty() and get_op_weight(c) <= get_op_weight(stack.top()):
                res += stack.pop()
            stack.push(c)
while not stack.is_empty():
    res += stack.pop()
print(res)
