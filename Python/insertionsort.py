def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

arr = [2, 1, 3, 7, 6]

insertionSort(arr)

for i in range(len(arr)):
    print ("% d" % arr[i])
