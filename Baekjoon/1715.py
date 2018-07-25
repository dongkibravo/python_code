import heapq
import sys

class Heap(object):
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        if len(self._heap)>0:
            return(heapq.heappop(self._heap))
        else:
            return None


heap = Heap()

r = lambda : int(sys.stdin.readline())
n = r()
for _ in range(n):
    key = r()
    heap.push(key)

# n = int(input())
# for i in range(n):
    # key = int(input())
    # heap.push(key)

# heap.push(10)
# heap.push(50)
# heap.push(40)
# heap.push(20)
# heap.push(60)
# heap.push(50)
#
# res = []
# while True:
#     val = heap.pop()
#     if val is None:
#         break
#     else:
#         res.append(val)
#
# print(res)
#
# heap.push(10)
# heap.push(50)
# heap.push(40)
# heap.push(20)
# heap.push(60)
# heap.push(50)


prev_val = 0
tot_sum = 0
while True:
    val = heap.pop()
    if val is None:
        break
    else:
        if prev_val == 0:
            prev_val = val
        else:
            prev_val += val
            tot_sum += prev_val
print(tot_sum)


#
# heap = Heap()
# n = int(input())
# for i in range(n):
#     key = int(input())
#     if key == 0:
#         print(heap.pop())
#     else:
#         heap.push(key)
