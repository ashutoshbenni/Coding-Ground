from random import randint
from time import time

def partition(arr, p, r):
    pivot = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    else:
        arr[i + 1],arr[r] = arr[r], arr[i + 1]
    print "pivot = %d" % (i + 1)
    print arr
    return i + 1

def quicksort(arr, p ,r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)
        
def main():
    arr = [randint(-1,10) for i in range(10)]
    print arr
    print "Applying quick sort..."
    start = time()
    quicksort(arr, 0, len(arr)- 1)
    print time() - start

if __name__ == "__main__":
    main()
