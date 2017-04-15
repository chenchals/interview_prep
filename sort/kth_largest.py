def kth_largest(li, k):
    k -= 1
    if k > len(li):
        raise Exception('k is larger then length of list')
    return _kth_largest_impl(li, 0, len(li)-1, k)

def _kth_largest_impl(li, l, r, k):
    if l > r:
        return
    pivot = l
    head = l
    tail = r
    l += 1
    while l < r:
        if li[r] <= li[pivot] < li[l]:
            li[r], li[l]  = li[l], li[r]
        if li[r] > li[pivot]:
            r -= 1
        if li[l] <= li[pivot]:
            l += 1
    li[pivot], li[r] = li[r], li[pivot]
    pivot = r
    if pivot > k:
        return _kth_largest_impl(li, head, pivot-1, k)
    elif pivot < k:
        return _kth_largest_impl(li, pivot+1, tail, k)
    elif pivot == k:
        return li[k]


t = [2,5,1,6,1,3,2,9]
print(kth_largest(t, 5))