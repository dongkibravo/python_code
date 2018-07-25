from queue_ import Queue

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def insert(self, data):
        if self.value:
            if data <= self.value:
                if self.left is None:
                    self.left = Tree()
                    self.left.value = data
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = Tree()
                    self.right.value = data
                else:
                    self.right.insert(data)
        else:
            self.value = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()

    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.value)
            res += self.preorder_traversal(root.left)
            res += self.preorder_traversal(root.right)
        return res

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.value)
            res += self.inorder_traversal(root.right)
        return res

    def postorder_traversal(self, root):
        res = []
        if root:
            res += self.postorder_traversal(root.left)
            res += self.postorder_traversal(root.right)
            res.append(root.value)
        return res

    def level_traversal(self, root):
        q = Queue()
        visited = []
        q.enqueue(root)
        while not q.is_empty():
            node = q.dequeue()
            visited.append(node.value)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return visited

root = Tree()
root.insert('F')
root.insert('B')
root.insert('G')
root.insert('A')
root.insert('D')
root.insert('I')
root.insert('C')
root.insert('H')
root.insert('E')


preorder = root.preorder_traversal(root)
inorder = root.inorder_traversal(root)
postorder = root.postorder_traversal(root)
level = root.level_traversal(root)

print("PRE")
print(preorder)
print("IN")
print(inorder)
print("POST")
print(postorder)
print("LEVEL")
print(level)
