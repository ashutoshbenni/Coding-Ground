from random import randint
from time import time
global limit 

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    left  = [0] * n1
    right = [0] * n2
    for i in range(0, n1):
        left[i] = arr[low + i]
    for j in range(0, n2):
        right[j] = arr[mid + j + 1]
    i = 0
    j = 0
    k = low
    while i < n1 and j <n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j <n2:
        arr[k] = right[j]
        j += 1
        k += 1
    
def split(arr, low, high, limit):
    if high - low < limit and high > low:
        n = high - low + 1
        insertionsort(arr, low, high)
    elif high > low:
        mid = (high + low - 1) / 2
        split(arr, low, mid, limit)
        split(arr, mid + 1, high, limit)
        merge(arr, low, mid, high)

def mergesort(arr, n):
    split(arr, 0, n, 10)
    
def insertionsort(arr, start, end):
    for j in range(start, end + 1):
        i = j - 1
        key = arr[j]
        while arr[i] > key and i >= start :
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    
def main():
    arr = [randint(1,10000) for i in xrange(100000)]
    start = time()
    mergesort(arr, len(arr) - 1)
    print arr
    print time() - start

if __name__ == "__main__":
    main()
