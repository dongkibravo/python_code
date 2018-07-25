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

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size()==0


def sortAscdening(stack, sorted_stack):
    if stack.is_empty():
        return sorted_stack
    else:
        val = stack.pop()
        if sorted_stack.is_empty():
            sorted_stack.push(val)
            return sortAscdening(stack, sorted_stack)
        else:
            val_sorted_stack = sorted_stack.pop()
            while not sorted_stack.is_empty() and val < val_sorted_stack:
                stack.push(val_sorted_stack)
                val_sorted_stack = sorted_stack.pop()

            if val>val_sorted_stack:
                sorted_stack.push(val_sorted_stack)
                sorted_stack.push(val)
            else:
                sorted_stack.push(val)
                sorted_stack.push(val_sorted_stack)

            return sortAscdening(stack, sorted_stack)

def sort_stack(stack):
    result = Stack()
    while stack.size() > 0:
        el = stack.pop()
        num_popped_from_result = 0
        while not result.is_empty() and result.peak() > el:
            stack.push(result.pop())
            num_popped_from_result += 1
        result.push(el)
        for i in range(num_popped_from_result):
            result.push(stack.pop())
    return result


st = Stack()

st.push(1)
st.push(5)
st.push(2)
st.push(4)
st.push(9)
st.push(3)
st.push(7)

empty_stack = Stack()
print(st.stack)
sorted_stack = sortAscdening(st, empty_stack)
print(sorted_stack.stack)
print("v2")
st.push(1)
st.push(5)
st.push(2)
st.push(4)
st.push(9)
st.push(3)
st.push(7)
sst = sort_stack(st)
print(sst.stack)
