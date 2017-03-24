from random import randint
from time import time


def partition(arr, p, r):
	pivot = arr[p]
	i = p - 1
	j = r + 1
	while True:
		j -= 1
		while j >= p and arr[j] > pivot:
			j -= 1
		i += 1
		while i <= r and arr[i] < pivot:
			i += 1
		if i < j:
			arr[i], arr[j] = arr[j], arr[i]
		else:
			return j

def tail_recursion_quick_sort(arr, p, r):
	while p < r:
		q = partition(arr, p, r)
		tail_recursion_quick_sort(arr, p, q)
		p = q + 1

def main():
	arr = [randint(-1,11) for i in range(9)]
	print arr
	start = time()
	print "Performing Tail Recursion Quick Sort..."
	tail_recursion_quick_sort(arr,0,len(arr) - 1)
	print arr
	print time() - start

if __name__ == "__main__":
	main()

