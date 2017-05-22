# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        self.build_heap(lists)
        ret = []
        for i in range(self.len):
            ret.append(self.pop_min())
        return ret

    def __init__(self):
        self.heap = list()
        self.tail = 0  # increment 1 before use tail
        self.head = 1
        self.len = 0



    def build_heap(self, lists):

        self.heap = [0 for _ in range(sum([len(x) if x else 0 for x in lists]))]
        self.len = len(self.heap)
        for nums in lists:
            for num in nums:
                self.insert(num)


    def insert(self, num):
        self.tail += 1  # increment 1 before use tail
        self.heap[self.tail] = num
        cur = self.tail
        parent = int(cur / 2)
        while parent > 0 and self.heap[parent] < self.heap[cur]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[cur]
            self.heap[cur] = tmp
            cur = parent
            parent = int(cur / 2)


    def pop_min(self):
        # print(self.heap, end='=')
        ret = self.heap[1]
        self.heap[1] = self.heap[self.tail]
        self.tail -= 1
        # print(self.heap, self.tail+1, end='=')
        head = 1
        left = int(2 * head) if int(2 * head) <= self.tail else None
        right = int(2 * head + 1) if int(2 * head + 1) <= self.tail else None
        if left is not None and right is not None:
            next = left if self.heap[left] > self.heap[right] else right
        else:
            next = left if left else right
            if not next:
                return ret
        while next <= self.tail and self.heap[next] > self.heap[head]:
            tmp = self.heap[head]
            self.heap[head] = self.heap[next]
            self.heap[next] = tmp
            head = next
            left = int(2 * head) if int(2 * head) <= self.tail else None
            right = int(2 * head + 1) if int(2 * head + 1) <= self.tail else None
            if left is not None and right is not None:
                next = left if self.heap[left] > self.heap[right] else right
            else:
                next = left if left else right
                if not next:
                    break
        # print(self.heap)
        return ret


t = Solution()
inputs = [[]]
t.mergeKLists(inputs)