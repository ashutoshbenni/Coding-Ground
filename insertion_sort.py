from time import time
from random import randint

def insertionsort(arr, n):
    for j in range(1,n):
        key = arr[j]
        i = j - 1
        while arr[i] > key and i > -1:
            arr[i + 1] = arr[i] 
            i -= 1
        arr[i + 1] = key
    
def main():
    print "enter a baunch of numbers..."
    arr = [randint(1,10000) for i in xrange(10000)]
    start = time()
    insertionsort(arr, len(arr))
    print arr
    print time() - start
    
    
if __name__ == "__main__":
    main()
