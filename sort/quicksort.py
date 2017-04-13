def quick_sort(li, l, r):
    print(li)
    if l >= r:
        return
    # l: start; r: end
    head = l
    tail = r
    pivot  = l
    l += 1
    # move the pointers
    while l < r:
        if li[l] < li[pivot]:
            l += 1
        if li[r] >= li[pivot]:
            r -= 1
        if li[l] < li[pivot] < li[r]:
            tmp = li[l]
            li[l] = li[r]
            li[r] = tmp
            # i'm moving this pointer again! don't do it!
            # l += 1
            # r -= 1
    # swap the value of pivot and l
    tmp = li[l-1]
    li[l-1] = li[pivot]
    li[pivot] = tmp
    pivot = l
    quick_sort(li, head, pivot-1)
    quick_sort(li, pivot, tail)

# there's a bug
l1 = [2,1,5,3,7]
quick_sort(l1, 0, 2)
print(l1)