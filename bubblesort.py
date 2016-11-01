


def bubble_sort(arr):

	print "start"
	arri = len(arr)
	while arri > 0:
		print arri
		for index in range (1, arri):
			if arr[index] < arr[index-1]:
				temp = arr[index]
				arr[index] = arr[index-1]
				arr[index-1] = temp
		print arr
		arri -= 1
	return arr



print bubble_sort([6, 5, 3, 1, 8, 7, 2, 4])