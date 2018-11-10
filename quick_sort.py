
def partition(lst, l, r):
	# print('Before partitioning:')
	# print(lst)
	# print('l:' + str(l))
	# print('r:' + str(r))
	p = lst[l] #pivot element is the first element
	i = l+1
	j = l+1
	while j <= r:
		if lst[j] < p:
			swap(lst, j, i)
			i += 1
		j += 1
	swap(lst, l, i-1)

	pivot_index_after_partition = i-1

	# print('After partitioning:')
	# print(lst)
	# print('p:' + str(pivot_index_after_partition))

	return pivot_index_after_partition


def chose_pivot(lst, l, r, strategy):
	if strategy == 'first':
		pivot_index = l
	elif strategy == 'last':
		pivot_index = r
	elif strategy == 'median_of_three':
		first = l
		middle = (l+r)//2
		last = r
		
		a = lst[first]
		b = lst[middle]
		c = lst[last]

		if a > b:
		    if a < c:
		        # median = a
		        pivot_index = first
		    elif b > c:
		        # median = b
		        pivot_index = middle
		    else:
		        # median = c
		        pivot_index = last
		else:
		    if a > c:
		        # median = a
		        pivot_index = first
		    elif b < c:
		        # median = b
		        pivot_index = middle
		    else:
		        # median = c
		        pivot_index = last

	return pivot_index

def swap(lst, index_a, index_b):
	temp = lst[index_a]
	lst[index_a] = lst[index_b]
	lst[index_b] = temp


def quick_sort(lst, l, r, comparisons, pivot_strategy):
	if r==l:
		return lst, comparisons
	else:
		pivot_index = chose_pivot(lst, l, r, pivot_strategy)

		#swap pivot with first element if needed
		if pivot_index != l:
			swap(lst, pivot_index, l)

		comparisons = comparisons + (r-l)

		pivot_index_after_partition = partition(lst, l, r)

		if pivot_index_after_partition > l:
			lst, comparisons = quick_sort(lst, l, pivot_index_after_partition-1, comparisons, pivot_strategy)

		if pivot_index_after_partition < r:
			lst, comparisons = quick_sort(lst, pivot_index_after_partition+1, r, comparisons, pivot_strategy)

		return lst, comparisons


# print(quick_sort([6,5,4,3,2,1],0,5,0,'first'))

def get_int_array(file_name):
	int_array = []

	file = open(file_name, 'r') 
	# print(file.read()) 


	string_array = file.readlines()
	int_array = list(map(int, string_array))
	# print(int_array)
	# print(len(int_array))
	# print(int_array[0])
	# print(int_array[-1])
	return int_array

int_array = get_int_array('QuickSort.txt')

# print(quick_sort(int_array, 0, len(int_array)-1, 0, 'first')[1])
# 155432
# 162085

# print(quick_sort(int_array, 0, len(int_array)-1, 0, 'last')[1])
# 157491
# 164123

print(quick_sort(int_array, 0, len(int_array)-1, 0, 'median_of_three')[1])
# 132671
# 138382