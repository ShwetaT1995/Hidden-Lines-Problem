import time

def find_visibleLines(list_of_m, list_of_b):
	length = len(list_of_m)

	if length > 3:

		visibleLines_m = []
		visibleLines_b = []

		# Adding 2 lines to Visible Lines list
		visibleLines_m.append(list_of_m[0])
		list_of_m.remove(list_of_m[0])
		visibleLines_b.append(list_of_b[0])
		list_of_b.remove(list_of_b[0])

		visibleLines_m.append(list_of_m[0])
		list_of_m.remove(list_of_m[0])
		visibleLines_b.append(list_of_b[0])
		list_of_b.remove(list_of_b[0])

		numVisible = 2

		for i in range(len(list_of_m)):
			prevIntersect = (visibleLines_b[numVisible-1] - visibleLines_b[numVisible-2]) / (visibleLines_m[numVisible-2] - visibleLines_m[numVisible-1])
			currIntersect = (list_of_b[i] - visibleLines_b[numVisible-2]) / (visibleLines_m[numVisible-2] - list_of_m[i])

			while currIntersect < prevIntersect:
				visibleLines_m.remove(visibleLines_m[numVisible-1])
				visibleLines_b.remove(visibleLines_b[numVisible-1])

				numVisible = numVisible - 1

				if numVisible == 1:
					break

				prevIntersect = (visibleLines_b[numVisible-1] - visibleLines_b[numVisible-2]) / (visibleLines_m[numVisible-2] - visibleLines_m[numVisible-1])
				currIntersect = (list_of_b[i] - visibleLines_b[numVisible-2]) / (visibleLines_m[numVisible-2] - list_of_m[i])

			visibleLines_m.append(list_of_m[i])
			visibleLines_b.append(list_of_b[i])
			numVisible += 1

		return visibleLines_m, visibleLines_b

	elif length == 3:

		# Sorting line by Slope(m) using Bubble Sort
		for i in range(2):

			for j in range(i+1, 3):

				if list_of_m[i] > list_of_m[j]:
					
					list_of_m[i], list_of_m[j] = list_of_m[j], list_of_m[i]
					list_of_b[i], list_of_b[j] = list_of_b[j], list_of_b[i]

		# Sorting line by Intercept(b) using Bubble Sort
		for i in range(2):

			for j in range(i+1, 3):

				if list_of_m[i] == list_of_m[j]:

					if list_of_b[i] < list_of_b[j]:

						list_of_m[i], list_of_m[j] = list_of_m[j], list_of_m[i]
						list_of_b[i], list_of_b[j] = list_of_b[j], list_of_b[i]

		# Adjusting Visible Lines
		if list_of_m[0] == list_of_m[1] and list_of_m[1] == list_of_m[2]:
			list_of_m.remove(list_of_m[1])
			list_of_b.remove(list_of_b[1])
			list_of_m.remove(list_of_m[2])
			list_of_b.remove(list_of_b[2])

		elif list_of_m[0] == list_of_m[1]:
			list_of_m.remove(list_of_m[1])
			list_of_b.remove(list_of_b[1])

		elif list_of_m[1] == list_of_m[2]:
			list_of_m.remove(list_of_m[2])
			list_of_b.remove(list_of_b[2])			

		else:
			first_second_intersection = (list_of_b[1] - list_of_b[0]) / (list_of_m[0] - list_of_m[1])
			first_third_intersection = (list_of_b[2] - list_of_b[0]) / (list_of_m[0] - list_of_m[2])

			if first_second_intersection > first_third_intersection:
				list_of_m.remove(list_of_m[1])
				list_of_b.remove(list_of_b[1])

	elif length == 2:
		
		if list_of_m[0] == list_of_m[1]:

				list_of_m.remove(list_of_m[1])
				list_of_b.remove(list_of_b[1])

	return list_of_m, list_of_b

if __name__ == "__main__":
	list_of_m = []
	list_of_b = []

	no_of_lines = int(input('Enter number of lines: '))
	
	for i in range(no_of_lines):
		m = float(input('Enter value of m: '))
		b = float(input('Enter value of b: '))

		list_of_m.append(m)
		list_of_b.append(b)

	start_time = time.time()

	# Sorting line by Slope(m) using Bubble Sort
	for i in range(no_of_lines):

		for j in range(i+1, no_of_lines):

			if list_of_m[i] > list_of_m[j]:

				list_of_m[i], list_of_m[j] = list_of_m[j], list_of_m[i]
				list_of_b[i], list_of_b[j] = list_of_b[j], list_of_b[i]

	# Sorting line by Intercept(b) using Bubble Sort
	for i in range(no_of_lines):

		for j in range(i+1, no_of_lines):

			if list_of_m[i] == list_of_m[j]:

				if list_of_b[i] < list_of_b[j]:

					list_of_m[i], list_of_m[j] = list_of_m[j], list_of_m[i]
					list_of_b[i], list_of_b[j] = list_of_b[j], list_of_b[i]

	visibleLines_m, visibleLines_b = find_visibleLines(list_of_m, list_of_b)

	end_time = time.time()

	for i in range(len(visibleLines_m)):
		print('y =', visibleLines_m[i],'x +',visibleLines_b[i])

	print('Time taken to solve Hidden Line Problem: ', end_time - start_time)
