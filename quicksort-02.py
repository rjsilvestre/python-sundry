# QUICKSORT ALGORITHM
# ===================
# This script was made for learning purposes based on the quicksort algorithm
# presented on Introduction to computer science, Udacity online course.
# It recursively creates two lists where elements are appended to the proper 
# list according to their value as lower or higher when compared to a pivot 
# value to later be concatenated as the result of the function.


def quicksort(array):
	if not array or len(array) <= 1:
		return array
	else:
		pivot = array[0]
		lower = []
		higher = []
		
		for e in array[1:]:
			if e <= pivot:
				lower.append(e)
			else:
				higher.append(e)
	
	return quicksort(lower) + [array[0]] + quicksort(higher)


# Test case

array = [9, 2, 6, 4, 3, 5, 1]
print (array)
print (quicksort(array))
