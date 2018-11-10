
def divide(lst):

	n = len(lst)

	n1 = n//2
	n2 = n-n1

	lst1 = lst[:n1]
	lst2 = lst[n1:]

	return lst1, lst2


def merge(lst1, lst2):
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
			j = j+1
			if j >= n2:
				merged_lst = merged_lst+lst1[i:]
				break

	return merged_lst


def merge_sort(lst):
	if len(lst)==1:
		return lst
	else:
		lst1, lst2 = divide(lst)
		lst1_sorted = merge_sort(lst1)
		lst2_sorted = merge_sort(lst2)
		return merge(lst1_sorted, lst2_sorted)


print(merge_sort([2,6,3,8,9,3,12,8,7,123,0,99,7,2,66,4,3,2,1]))


