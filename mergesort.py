def merge2(array, l, m, r):
    arr1 = array[l:m]
    arr2 = array[m:r + 1]
    i, j = 0, 0
    ind = l
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            array[ind] = arr1[i]
            ind += 1
            i += 1
        else:
            array[ind] = arr2[i]
            ind += 1
            j += 1
    while i < len(arr1):
        array[ind] = arr1[i]
        i += 1
        ind += 1
    while j < len(arr2):
        array[ind] = arr2[j]
        j += 1
        ind += 1


def mergeSort2(array, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    mergeSort2(array, l, mid)
    mergeSort2(array, mid + 1, r)
    merge2(array, l, mid, r)


a = [2, 3, 1, 5, 4, 6]
mergeSort2(a, 0, len(a) - 1)
print(a)
