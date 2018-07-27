# Space Complexity O(1)
# Time Complexity O(N^2)

class Bubble(object):
    def __init__(self, array):
        self.array = array

    def length(self):
        return len(self.array)

    def ascending_sorted(self):
        asc_sorted = self.array
        arr_len = self.length()
        for x in range(arr_len-1):
            for x in range(arr_len-1-x):
                if asc_sorted[x] > asc_sorted[x+1]:
                    asc_sorted[x], asc_sorted[x+1] = asc_sorted[x+1], asc_sorted[x]
        return asc_sorted

    def descending_sorted(self):
        dsc_sorted = self.array
        arr_len = self.length()
        for x in range(arr_len-1):
            for x in range(arr_len-1-x):
                if dsc_sorted[x] < dsc_sorted[x+1]:
                    dsc_sorted[x], dsc_sorted[x+1] = dsc_sorted[x+1], dsc_sorted[x]
        return dsc_sorted


a = [7, 4, 11, 9, 2]
bubble = Bubble(a)
print(bubble.array)
print(bubble.ascending_sorted())
print(bubble.descending_sorted())
