from random import randint

def quick_sort(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot=a[randint(0, len(a)-1)]

    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort(smaller)+equal+quick_sort(larger)

def quick_sort2(a):
    if len(a) <= 1:
        return a
    smaller, equal, larger = [], [], []
    pivot=a[randint(0, len(a)-1)]
    print("piv: "+str(pivot))
    for x in a:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort2(larger)+equal+quick_sort2    (smaller)


a = [5, 9, 1, 2, 4, 8, 6, 3, 7]
sorted = quick_sort(a)
sorted2 = quick_sort2(a)
print(a)
print(sorted)
print(sorted2)
