class Stack:
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
        return self.size()==0


class Queue:
    def __init__(self):
        self.enq_stack = Stack()
        self.deq_stack = Stack()

    def push(self, val):
        self.enq_stack.push(val)

    def pop(self):
        if self.deq_stack.is_empty():
            if self.enq_stack.is_empty():
                return None
            else:
                self.pop_and_push()

        return self.deq_stack.pop()

    def pop_and_push(self):
        while not self.enq_stack.is_empty():
            self.deq_stack.push(self.enq_stack.pop())
        return


queue = Queue()
print(queue.pop())
queue.push(1)
queue.push(2)
print(queue.pop())
queue.push(5)
print(queue.pop())
print(queue.pop())
