
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next

    def removeDuplicates(self):
        node = self
        numList = []
        prevNode = None

        while node != None:
            if node.val in numList:
                prevNode.next = node.next
            else:
                numList.append(node.val)
                prevNode = node
            node = node.next

    def getKth(self, k):
        n = 1
        node = self
        while n < k:
            print(node.val)
            node = node.next
            n += 1
            if node.next == None:
                return False

        return node

    def deleteKth(self,k):
        n = 1
        node = self
        prevNode = None
        while n <k:
            prevNode = node
            node = node.next
            n += 1
            if node.next == None:
                print("Out of range")
                return False
        prevNode.next = node.next

    def getLeft2Right(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            node = node.next
        return int(output)

    def getRight2Left(self):
        node = self
        output = ''
        while node != None:
            output =str(node.val)+output
            node = node.next

        return int(output)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)

node5 = Node(4)
node6 = Node(2)
node7 = Node(5)

node1.next = node2
node2.next = node3
# node3.next = node4

node4.next = node5
node5.next = node6
node6.next = node7

node1.traverse()
node4.traverse()

#left to right sum
n1Num = node1.getLeft2Right()
n4Num = node4.getLeft2Right()
print(n1Num)
print(n4Num)
print(n1Num+n4Num)
print(" ")
print(" ")
#right to left sum
x = node1.getRight2Left()
y = node4.getRight2Left()
print(x)
print(y)
print(x+y)





# node1.traverse()
# node1.removeDuplicates()



# n4 = node1.getKth(4)
# print("------")
# print(n4.val)

# node1.deleteKth(5)
# node1.traverse()
