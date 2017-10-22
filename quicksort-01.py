# This script was made for learning purposes based on some online research.
# It uses a single list where elements are recursively swaped according to 
# their value to the left(lower) or right(higher) when compared to a pivot
# value.


def quicksort(array, left, right):
    '''
    Sorts a list of values using quicksort algorithm.

    Args:
        array: List of values.
        left: The left start position for the comparison.
        rigth: The right start position for the comparison.
    
    Returns:
        The sorted array.
    '''
    if left >= right:
        return
    pivot = array[left]
    index = partition(array, left, right, pivot)	
    quicksort(array, left, index - 1)
    quicksort(array, index, right)
    return array

def partition(array, left, right, pivot):
    '''
    Moves all the smaller values to the left of the pivot
    and all the bigger values to the right of the pivot.

    Args:
        array: List of values.
        left: The left start position for the comparison.
        rigth: The right start position for the comparison.
        pivot: The value to be compared.

    Returns:
        The array after all the values arranged.
    '''
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
