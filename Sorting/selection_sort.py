class Selection(object):
    def __init__(self, arr):
        self.array = arr

    def length(self):
        return len(self.array)

    def asc_sort(self):
        len = self.length()
        asc_arr = self.array
        for i in range(len):
            min = i
            for x in range(i+1, len):
                if asc_arr[x] < asc_arr[i]:
                    min = x
            asc_arr[i], asc_arr[min] = asc_arr[min], asc_arr[i]
        return asc_arr

    def dsc_sort(self):
        len = self.length()
        dsc_arr = self.array
        for i in range(len):
            max = i
            for x in range(i+1, len):
                if dsc_arr[x]> dsc_arr[i]:
                    max = x
            dsc_arr[i], dsc_arr[max] = dsc_arr[max], dsc_arr[i]
        return dsc_arr


a = [7, 4, 11, 9, 2]
selection = Selection(a)
print(selection.array)
print(selection.asc_sort())
print(selection.dsc_sort())
