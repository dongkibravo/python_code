import copy
import heapq

class Heap:
    # Min Heap
    def __init__(self, arr):
        self.array = copy.deepcopy(arr)

    def heapify(self):
        for i in range(1, len(self.array)):
            c = i
            while True:
                root = (c-1)//2
                if self.array[root] > self.array[c]:
                    temp = self.array[root]
                    self.array[root] = self.array[c]
                    self.array[c] = temp
                c = root
                if c==0:
                    break

    def sort_descending(self):
        arr = copy.deepcopy(self.array)
        arr_len = len(arr)
        for i in reversed(range(1, arr_len)):
            temp = arr[i]
            arr[i] = arr[0]
            arr[0] = temp
            root = 0
            while True:
                c = 2*root+1
                if c<(i-1) and arr[c]>arr[c+1]:
                    c+=1
                if c<i and arr[root]>arr[c]:
                    temp = arr[root]
                    arr[root] = arr[c]
                    arr[c] = temp
                root = c
                if c>i:
                    break
        return arr

        # Ascending for Max Heap
        """
        for i in reversed(range(1,len(arr))):
            temp = arr[i]
            arr[i] = arr[0]
            arr[0] = temp
            root = 0
            print(arr)
            print("******")
            while True:
                c = 2*root+1
                if c<(i-1) and arr[c] < arr[c+1]:
                    c+=1
                if c<i and arr[c] < arr[root]:
                    temp = arr[root]
                    arr[root] = arr[c]
                    arr[c] = temp
                root = c
                print(arr)
                if c>i:
                    break
        return arr
        """

    def insert_key(self, key):
        child =  len(self.array)
        self.array.append(key)
        while True:
            root = child // 2
            if self.array[root] > self.array[child]:
                temp = self.array[root]
                self.array[root] = self.array[child]
                self.array[child] = temp
            child = root
            if root == 0:
                break

    def remove_key(self, key):
        i = len(self.array)
        r = key
        while True:
            child = 2*r+1
            if child<i-1 and self.array[child] > self.array[child+1]:
                child+=1
            if child<i:
                self.array[r] = self.array[child]
            r = child
            if 2*r+1 > i:
                del self.array[r]
                break


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def insertKey(self, k):
        heapq.heappush(self.heap, k)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i] , self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]

    def extractMin(self):
        return heapq.heappop(self.heap)

    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

arr = [7,6,5,8,3,5,9,1,6]

heap = Heap(arr)
heap.heapify()
# heap.insert_key(3)
print(heap.array)
# print(" ----- ")
# print(" ----- ")
# print(" ----- ")
# heap.remove_key(1)
# print(heap.array)

print("python wayyyyyyyyyyyyyyyyy")
print(arr)
heapq.heapify(arr)
print(arr)


print("python internal heap function")

heapObj = MinHeap()
heapObj.insertKey(3)
heapObj.insertKey(2)
heapObj.deleteKey(1)
heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.heap)

print(heapObj.extractMin())
print(heapObj.getMin())
heapObj.decreaseKey(2, 1)
print(heapObj.getMin())
