def merge_sort(arr):

	length = len(arr)

	if(length < 2):

		return arr 
		#if length of array is less than 2 we simply return the array

	else:

		a = arr[:length/2] #take the first half (if odd it will take smaller part)
		b = arr[length/2:] #take the remaining part

		a = merge_sort(a) #recursively calling this till we have a and b cut down to the smallest length
		b = merge_sort(b)	


		final = [] #output array

		while len(a) !=0 and len(b) !=0:

			if a[0] < b[0]:
				final.append(a[0])
				a.remove(a[0])
			else:
				final.append(b[0])
				b.remove(b[0])

		#if len(a) was less than len(b) or vice-versa, then we simply append remaining b to existing final as there is nothing to
		#compare		
		if len(a) == 0:
			final += b  
		else:
			final += a
		
	    
		return final
		
length_of_array = int(raw_input("Enter length of array:"))

my_array = []

for i in xrange(length_of_array):
    my_array.append(int(raw_input('Enter %d of array: ' %(i))))


print "Input unsorted array",my_array  # Shows you the results

print "output array after merge sort",merge_sort(my_array) #final output after merge sort