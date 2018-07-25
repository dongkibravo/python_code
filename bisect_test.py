import bisect
import sys

print(sys.version)

a = list(map(int, input("enter numbers: ").split(',')))

a.sort()
print(a)
val = int(input("enter a value: "))
print(val)
answer = bisect.bisect(a, val)
print(answer)
