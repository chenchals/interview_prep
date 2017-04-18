'''
Binary search is still a problem
When checking crossover, allow overlap l>=r
'''

def search_rotated_array(li, v):
    if len(li) == 0:
        return -1
    # find pivot point
    p = _find_pivot(li, 0, len(li)-1)
    print(p)
    if v > li[-1]:
        # search left half [0, p)
        return _binary_search(li, 0, p, v)
    else:
        # search right half [p, len(li))
        return _binary_search(li, p, len(li), v)

def _binary_search(li, l, r, v):
    # allow overlap! before was break when l>r, this is wrong because median always round down
    if l >= r:
        return -1
    m = int((l+r)/2)
    if li[m] == v:
        return m
    if v < li[m]:
        return _binary_search(li, l, m, v)
    else:
        return _binary_search(li, m+1, r, v)

def _find_pivot(li, l, r):
    if l >= r:
        return l
    r_v = li[r]
    m = int((l+r)/2)
    if m+1 < len(li):
        if li[m+1] < li[m]:
            return m+1
        if li[m] < r_v:
            return _find_pivot(li, l, m)
        else:
            return _find_pivot(li, m+1, r)
    else:
        return l
    # print(p)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return search_rotated_array(nums, target)

if __name__ == "__main__":

    li = [3,1]
    assert search_rotated_array(li, 3) == 0


    li = [3,6,8,0,1]
    # print(search_rotated_array(li, 3))
    # exit()
    assert search_rotated_array(li, 3) == 0
    assert search_rotated_array(li, 0) == 3
    assert search_rotated_array(li, 8) == 2
    li = [1,6,8,16,0]
    assert search_rotated_array(li, 0) == 4


