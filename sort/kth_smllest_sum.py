

def return_kth_sum(l1, l2, k):
	i, j = 0,0
	idx_k = 0
	summation = 0
	while idx_k < k:
		idx_k += 1
		summation = l1[i] + l2[j]
		if l1[i] + l2[j+1] < l1[i+1] + l2[0]:
			j += 1
		else:
			i += 1
			j = 0
	return summation



if __name__ == "__main__":
	list1 = [1,2,3,6]
	list2 = [3,5,8, 10]
	ret = return_kth_sum(list1, list2, 3)
	print(ret)