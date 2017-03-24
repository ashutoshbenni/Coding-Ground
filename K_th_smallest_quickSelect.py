from random import randint
from time import time

def partition(arr,p,r):
    pivot = arr[r]
    i = p - 1
    for j in range(p,r):#using Lomuto's partition method...
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] =arr[j],arr[i]
    arr[i + 1],arr[r] = arr[r],arr[i + 1]
    return i + 1

def quickselect(arr,p,r,key):
    if p < r:
        q = partition(arr,p,r)
        if q  == key: # If partition index is equal to kth number stop...
            return
        elif q > key - 1: 
            quickselect(arr,p,q-1,key)
        else:
            quickselect(arr,q+1,r,key)

def main():
    arr = [randint(-1,1000000) for i in range(1000000)]#picking numbers randomly 
    print "Which smallest number you want to you wnat to find an above array?"
    k = int(raw_input())
    if k > len(arr):# k should be less than the length of input...
        start = time()
        raise "Invalid input: Exceeds the array limit ERROR."
    else:
        start = time()#calculate the time to find kth smallest
        print "finding %dth smallest element..." % k
        quickselect(arr,0,len(arr)-1,k-1)
        #print arr
        print arr[k-1]
    print time() - start

if __name__ == "__main__":#execution will start from here...
    main()
