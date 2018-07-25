class MaxHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self.__floatUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap) > 1:
            self.__swap(0, len(self.heap)-1)
            max = self.heap.pop()
            self.__bubbleDown(0)
        elif len(self.heap) == 1:
            max = self.heap.pop()
        else:
            max = 0
        return max

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent = (index-1)//2
        if index == 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        root = index
        child = index*2
        if len(self.heap)-1 > child and self.heap[child+1] > self.heap[child]:
            child = child + 1
        if root > child:
            self.__swap(root, child)
            self.__bubbleDown(child)


max_heap = MaxHeap()
n = int(input())
popped = []
for i in range(n):
    val = int(input())
    if val == 0:
        # print(max_heap.pop())
        popped.append(max_heap.pop())
    else:
        max_heap.push(val)

print(max_heap.heap)
print(popped)
