def merge_asc(left, right):
    list = []
    l = 0
    r = 0
    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            list.append(left[l])
            l+=1
        else:
            list.append(right[r])
            r+=1
    list += left[l:]
    list += right[r:]
    return list

def merge_dsc(left, right):
    list = []
    l = 0
    r = 0
    while l<len(left) and r<len(right):
        if left[l]>right[r]:
            list.append(left[l])
            l+=1
        else:
            list.append(right[r])
            r+=1
    list += left[l:]
    list += right[r:]
    return list


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    return merge_asc(left, right)

def merge_sort2(list):
    if len(list) <= 1:
        return list
    mid = len(list)//2
    left = merge_sort2(list[:mid])
    right = merge_sort2(list[mid:])
    return merge_dsc(left, right)

a = [7, 4, 11, 9, 2]
sorted_asc = merge_sort(a)
sorted_dsc = merge_sort2(a)
print(a)
print(sorted_asc)
print(sorted_dsc)
