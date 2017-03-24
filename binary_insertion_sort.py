from time import time
from random import randint

def insertion_sort(arr, n):
    
    for j in range(1, n):
        key = arr[j]
        i = j - 1
        low = 0
        high = j
        while low < high:
            mid = (low + high) // 2
            if key >= arr[mid]:
                low = mid + 1
            else:
                high = mid
        while i >= low:
            arr[i + 1]= arr[i]
            i -= 1
        arr[i + 1] = key
        

def main():
    
    arr = [randint(-10,10) for i in range(8)]
    print (arr)
    insertion_sort(arr, len(arr))
    print (arr)
if __name__ == "__main__":
    main()
    
"""
def binarysearch(arr, key, low, high):
    if high <= low:
        if key > arr[low]:
            return low + 1
        return low
    mid = (low + high) / 2
    if key == arr[mid]:
        return mid + 1
    if key < arr[mid]:
        return binarysearch(arr, key, low, mid - 1)
    return binarysearch(arr, key, mid + 1, high)

def insertionsort(arr, n):
    for j in range(1, n):
        i = j - 1
        key = arr[j]
        pos = binarysearch(arr, key, 0, i)
        while i >= pos:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

def main():
    print "Enter a bunch of numbers..."
    arr = [randint(1,100000) for i in xrange(10000)]
    start = time()
    insertionsort(arr, len(arr))
    print arr
    print time() - start

if __name__ == "__main__":
    main()
"""
