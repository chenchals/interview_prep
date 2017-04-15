def kth_largest(li, k):
    k -= 1
    if k < 0:
        raise Exception('k has to be positive value')
    if k > len(li):
        raise Exception('k is larger then length of list')
    return _kth_largest_impl(li, 0, len(li)-1, k)

def _kth_largest_impl(li, l, r, k):
    if l >= r:
        return li[min(l,r)]
    pivot = l
    head = l
    tail = r
    l += 1
    # print(li)
    # why <=???????????????
    while l <= r:
        stop_right = li[r] <= li[pivot]
        stop_left = li[pivot] < li[l]
        if stop_right and stop_left:
            li[r], li[l]  = li[l], li[r]
        if not stop_right:
            r -= 1
        if not stop_left:
            l += 1
    li[pivot], li[r] = li[r], li[pivot]
    pivot = r
    # print(l,r,li,k)
    if pivot == k:
        return li[pivot]
    elif pivot > k:
        return _kth_largest_impl(li, head, pivot-1, k)
    elif pivot < k:
        return _kth_largest_impl(li, pivot+1, tail, k)



import random
epoch = 100
k = 99
for _ in range(epoch):
    query = [random.randint(1,100) for _ in range(100)]
    answer = sorted(query)[k-1]
    my_answer = kth_largest(query, k)
    if answer != my_answer:
        raise Exception(query, answer, my_answer)

