# 맞았습니다
import heapq
class Heap(object):
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        res = 0
        if len(self._heap)>0:
            res = heapq.heappop(self._heap)
        return res

heap = Heap()
n = int(input())
for i in range(n):
    key = int(input())
    if key == 0:
        print(heap.pop())
    else:
        heap.push(key)
