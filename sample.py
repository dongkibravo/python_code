a = [1,4,23,125,3253,123,4523,12,4]
a.sort()

def BinarySearch(arr, value, low, high):
    print("ch")
    mid = (low+high)//2
    if arr[mid]>value:
        return BinarySearch(arr, value, low, mid-1)
    elif arr[mid]<value:
        return BinarySearch(arr, value, mid+1, high)
    else:
        return mid

val = int(input("Enter a value: "))

result = BinarySearch(a, val, 0, len(a)-1)

print(result)
print(a)
