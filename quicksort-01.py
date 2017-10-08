# QUICKSORT ALGORITHM
# ===================
# This script was made for learning purposes based on some online research.
# It uses a single list where elements are recursively swaped according to 
# their value to the left(lower) or right(higher) when compared to a pivot
# value.


def quicksort(array, left, right):

	if left >= right:
		return

	pivot = array[left]
	index = partition(array, left, right, pivot)	
	
	quicksort(array, left, index - 1)
	quicksort(array, index, right)

	return array


def partition(array, left, right, pivot):
	
	while left <= right:
		while array[left] < pivot:
			left += 1
	
		while array[right] > pivot:
			right -= 1
	
		if left <= right:
			array[left], array[right] = array[right], array[left]
			left += 1
			right -= 1		

	return left


# Test case

array = [9, 2, 6, 4, 3, 5, 1]
print (array)
print (quicksort(array, 0, len(array) - 1))
