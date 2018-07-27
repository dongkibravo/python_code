class Insertion(object):
    def __init__(self, arr):
        self.array = arr

    def length(self):
        return len(self.array)

    def asc_sort(self):
        asc_arr = self.array
        len = self.length()
        for i in range(len):
            pos = i
            for x in reversed(range(i-1)):
                if asc_arr[pos] > asc_arr[x]:
                    break
                else:
                    asc_arr[pos], asc_arr[x] = asc_arr[x], asc_arr[pos]
                    pos = x

        return asc_arr

    def dsc_sort(self):
        dsc_arr = self.array
        len = self.length()
        for i in range(len):
            pos = i
            for x in reversed(range(i-1)):
                if dsc_arr[pos] < dsc_arr[x]:
                    break
                else:
                    dsc_arr[pos], dsc_arr[x] = dsc_arr[x], dsc_arr[pos]
                    pos = x

        return dsc_arr


a = [7, 4, 11, 9, 2]
insertion = Insertion(a)
print(insertion.array)
print(insertion.asc_sort())
print(insertion.dsc_sort())
