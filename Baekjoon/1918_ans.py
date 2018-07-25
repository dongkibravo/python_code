# Right answer for 1918
import sys

r = lambda : sys.stdin.readline()
input = str(r().strip())
stack = []
answer = ''
for c in input:
    if c.isalpha():
        answer += c
    else:
        while stack:
            if stack[-1] in ['*','/'] and c not in ['(',')']:
                answer += stack.pop()
            elif stack[-1] in ['+','-'] and c in ['+', '-']:
                answer += stack.pop()
            else:
                break
        if c != ')':
            stack.append(c)
        if c == ')':
            while True:
                p = stack.pop()
                if p == '(': break
                answer += p
while stack:
    answer += stack.pop()
print(answer)
