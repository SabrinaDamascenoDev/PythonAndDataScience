lista = [9,5,6,3,7,4,8,1,2,10]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range (0, n-i-1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(lista))