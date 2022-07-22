def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
arr = [5,3,8,6,7,1]
print(arr)
print(bubble_sort(arr))