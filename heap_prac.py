tree = [7,6,5,8,3,5,9,1,6]
# Max Heap
for i in range(1, len(tree)):
    c = i
    while True:
        root = (c-1) // 2
        if tree[root] < tree[c]:
            temp = tree[root]
            tree[root] = tree[c]
            tree[c] = temp
        c = root
        if c is 0:
            break


# Min Heap
for i in range(1, len(tree)):
    c = i
    while True:
        root = (c-1) // 2
        if tree[root] > tree[c]:
            temp = tree[root]
            tree[root] = tree[c]
            tree[c] = temp
        c = root
        if c is 0:
            break


print(tree)


# Ascending sort

for i in reversed(range(1, len(tree))):
    temp = tree[0]
    tree[0] = tree[i]
    tree[i] = temp
    root = 0
    # c = 1
    while True:
        c = 2*root+1
        if c<(i-1) and tree[c] < tree[c+1]:
            c+=1
        if c<i and tree[root] < tree[c]:
            temp = tree[root]
            tree[root] = tree[c]
            tree[c] = temp

        root = c

        if c>i:
            break

print(tree)
