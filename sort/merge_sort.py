def merge_sort(li):
    copy = li[:]
    _merge_sort(copy, 0, len(copy)-1)
    return copy

def _merge_sort(li, l, r):
    # in place swap
    # base condition, return when cross over
    if l >= r:
        return
    m = int((l+r)/2)
    if l <= m:
        _merge_sort(li, l, m)
    if m+1 <= r:
        _merge_sort(li, m+1, r)
    _merge(li, l, m, m+1, r)
    pass

def _merge(li, l1, r1, l2, r2):
    buffer = list(range(r2-l1+1))
    head = l1
    p = 0
    while l1 <= r1 and l2 <= r2:
        if li[l1] < li[l2]:
            buffer[p] = li[l1]
            l1 += 1
            p += 1
        else:
            buffer[p] = li[l2]
            l2 += 1
            p += 1
    while l1 <= r1:
        buffer[p] = li[l1]
        l1 += 1
        p += 1
    while l2 <= r2:
        buffer[p] = li[l2]
        l2 += 1
        p += 1
    for i in range(len(buffer)):
        li[head+i] = buffer[i]


import random
for _ in range(1000):
    test = [random.randint(0,10) for _ in range(8)]
    answer = sorted(test)
    my_answer = merge_sort(test)
    # print(test, answer, my_answer)
    if answer != my_answer:
        raise Exception(test, answer, my_answer)

