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

array = [9, 2, 6, 4, 3, 5, 1]
print (array)
print (quicksort(array))
