def Sort(arr):
    n = len(arr)
    count = 0

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count +=1
    return count

arr = [1,0,1,0,0,0,1,1,1]

t = Sort(arr)
print(t)