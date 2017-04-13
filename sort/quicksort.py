
# todo @charles rewrite this, the 1st practice produced so many bugs!!!
def quick_sort(li, l, r, verbose=False):
    if verbose:
        print('init:',l,r, li)
    # print(li)
    if l >= r:
        return
    # l: start; r: end
    head = l
    tail = r
    pivot  = l
    # l += 1
    if verbose:
        print('summary', head,tail,pivot,l,r)
    # move the pointers
    while l < r:
        if verbose:
            print(pivot,l,r,end=' ')
        if li[r] < li[pivot] < li[l]:
            tmp = li[l]
            li[l] = li[r]
            li[r] = tmp
            # i'm moving this pointer again! don't do it!
            l += 1
            r -= 1
        if li[l] <= li[pivot]:
            l += 1
        if li[r] >= li[pivot]:
            r -= 1
        if verbose:
            print(l,r)
        # print(li)
    # swap the value of pivot IN VALID case
    if li[pivot] > li[r]:
        tmp = li[r]
        li[r] = li[pivot]
        li[pivot] = tmp
        # only increment after swap
        pivot = r
    if verbose:
        print(li)
    quick_sort(li, head, pivot-1, verbose=verbose)
    # i forgot to increment right pointer. Once we sorted current pivot, leave current pivot untouched and sort rest of array
    quick_sort(li, pivot+1, tail, verbose=verbose)

# there's a bug
l1 = [3,3,1,3]
print(l1)
quick_sort(l1, 0, len(l1)-1, verbose=False)
print(l1)