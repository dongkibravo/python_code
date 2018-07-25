import heapq

class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, child):
        return (child-1)//2

    def size(self):
        return len(self.heap)

    def insertKey(self, key):
        child =  len(self.heap)
        self.heap.append(key)
        while True:
            root = child // 2
            if self.heap[root] > self.heap[child]:
                temp = self.heap[root]
                self.heap[root] = self.heap[child]
                self.heap[child] = temp
            child = root
            if root == 0:
                break

    def heappop(self):
        i = len(self.heap)-1
        r = 0
        res = self.heap[0]
        while True:
            child = 2*r+1
            if child > i:
                del self.heap[r]
                break
            else:
                if child<i-1 and self.heap[child] > self.heap[child+1]:
                    child+=1
                self.heap[r] = self.heap[child]
                r = child
        return res

heap = Heap()
n = int(input())
for i in range(n):
    key = int(input())
    if key == 0:
        if heap.size() == 0:
            print(0)
        else:
            print(heap.heappop())
    else:
        heap.insertKey(key)
