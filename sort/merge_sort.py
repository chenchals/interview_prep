def merge_sort(li):
    copied = li[:]
    _merge_sort(copied, 0, len(copied)-1)
    return copied

def _merge_sort(li, l, r):
    # base case
    if l >= r:
        return
    # split
    m = int((l+r)/2)
    _merge_sort(li, l, m)
    _merge_sort(li, m+1, r)
    # merge
    _merge(li, l, m, m+1, r)

def _merge(li, l1, r1, l2, r2):
    head, tail = l1, r2
    buffer = [0 for _ in range(l1, r2+1)]
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
    # Was a bug here, I forgot to add the offset of head to the li
    for i in range(len(buffer)):
        li[i+head] = buffer[i]


import random
for _ in range(1000):
    test = [random.randint(0,100) for _ in range(100)]
    answer = sorted(test)
    my_answer = merge_sort(test)
    # print(test, answer, my_answer)
    if answer != my_answer:
        raise Exception(test, answer, my_answer)

