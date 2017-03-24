from time import time
import random

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid
    left = arr[low :mid + 1]
    right = arr[mid + 1: high + 1]
    i = 0
    j = 0
    k = low
    while i < n1 and j < n2:
        if left[i] >= right[j]:
            arr[k] = right[j]
            j += 1
            k += 1
        else:
            arr[k] = left[i]
            i += 1
            k += 1
    while i < n1:
        arr[k] = left[i]
        k += 1
        i +=1
    while j < n2:
        arr[k] = right[j]
        k += 1
        j += 1
    
def mergesort(arr, low, high):
    if low < high:
        mid = (high + low) // 2
        mergesort(arr, low, mid)
        mergesort(arr, mid + 1, high)
        merge(arr, low, mid, high)


def main():
    arr = [random.randint(1,100) for i in xrange(10)]
    print (arr)
    start = time()
    mergesort(arr, 0, 9)
    print (arr)
    print (time() - start)
    

if __name__ == "__main__":
    main()
    

