
def divide(lst):

	n = len(lst)

	n1 = n//2
	n2 = n-n1

	lst1 = lst[:n1]
	lst2 = lst[n1:]

	return lst1, lst2


def merge(lst1, lst2, inversions):

	merged_lst = []

	n1 = len(lst1)
	n2 = len(lst2)

	n = n1+n2

	i = 0
	j = 0

	for x in range(n):
		if lst1[i]<lst2[j]:
			merged_lst.append(lst1[i])
			i = i+1
			if i >= n1:
				merged_lst = merged_lst+lst2[j:]
				break
		else:
			merged_lst.append(lst2[j])
			inversions = inversions + (n1-i)
			j = j+1
			if j >= n2:
				merged_lst = merged_lst+lst1[i:]
				break

	return merged_lst, inversions


def merge_sort(lst, inversions):
	if len(lst)==1:
		return lst, inversions
	else:
		lst1, lst2 = divide(lst)
		lst1_sorted, inversions = merge_sort(lst1, inversions)
		lst2_sorted, inversions = merge_sort(lst2, inversions)
		return merge(lst1_sorted, lst2_sorted, inversions)


print(merge_sort([6,5,4,3,2,1],0))

def get_int_array(file_name):
	int_array = []

	file = open(file_name, 'r') 
	# print(file.read()) 


	string_array = file.readlines()
	int_array = list(map(int, string_array))
	print(int_array)
	print(len(int_array))
	# print(int_array[0])
	# print(int_array[-1])
	return int_array

int_array = get_int_array('IntegerArray.txt')

print(merge_sort(int_array,0)[1])