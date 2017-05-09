def fit(placeholder, pos):
    start, end = pos
    bak = placeholder[:]
    for i in range(start, end):
        j = i
        while j >= len(placeholder):
            placeholder.append(False)
        if placeholder[i]:
            # nonlocal placeholder
            placeholder[:] = bak[:]
            return False
        else:
            placeholder[i] = True
    return True

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        count = 0
        queue = intervals
        while len(queue):
            pass
    def find_max_meetings(self, available, queue):
        pass
# count = 0
# while queue not empty:
#   first: find the maximum number of meeting a given time can have [0,n)
#   increase n until no more room to fit more meetings
#   remember the index of scheduled meetings, remove the them from queue
#   count += 1
# return count


placeholder = [False for _ in range(2)]
placeholder[0] = True
placeholder = [True]
print(placeholder)
ret = fit(placeholder, [3,4])
print(placeholder, ret)
ret = fit(placeholder, [2,4])
print(placeholder, ret)
