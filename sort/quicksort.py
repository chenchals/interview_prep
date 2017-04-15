
def quick_sort(li):
    copied = li[:]
    quick_sort_recursive(copied, 0, len(copied)-1)
    return copied

def quick_sort_recursive(li, l, r):
    if l >= r:
        return
    head = l
    tail = r
    pivot = l
    l += 1
    while l <= r:
        if li[r] <= li[pivot] < li[l]:
            li[l], li[r] = li[r], li[l]
        if li[pivot] < li[r]:
            r -= 1
        if li[pivot] >= li[l]:
            l += 1
    li[pivot], li[r] = li[r], li[pivot]
    pivot = r
    quick_sort_recursive(li, head, pivot-1)
    quick_sort_recursive(li, pivot+1, tail)

import random
epoch = 10
for _ in range(epoch):
    query = [random.randint(0, 5) for _ in range(10)]
    answer = sorted(query)
    print(query, end='-')
    my_answer = quick_sort(query)
    print(query, answer, my_answer)
    if answer != my_answer:
        raise Exception(query, answer, my_answer)
