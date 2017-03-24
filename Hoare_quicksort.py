from random import randint
def partition(arr, p ,r):
    pivot = arr[p]
    i = p - 1
    j = r + 1
    while True:
        j -= 1
        while j >= p and arr[j] > pivot :
            j -= 1
        i += 1
        while i <= r  and arr[i] < pivot:
            i += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            #arr[p], arr[j] = arr[j], arr[p] don't need to do this since we are calling quicksort [p,q] & (q,r]...
            return j

def quicksort(arr, p ,r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q)
        quicksort(arr, q + 1, r)

def main():
    arr = [randint(-1,10) for i in range(9)]
    print arr
    print "applying Hoare's partition Quick Sort..."
    quicksort(arr,0,len(arr) - 1)
    print arr

if __name__ == "__main__":
    main()
