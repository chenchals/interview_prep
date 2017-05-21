class Solution(object):
    def __init__(self):
        self.heap = list()
        self.tail = 0 # increment 1 before use tail
        self.head = 1

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        self.build_heap(nums)
        ret = 0
        for i in range(k):
            ret = self.pop_min()
        return ret

    def build_heap(self, nums):
        self.heap = [0 for _ in range(len(nums)+1)]
        for num in nums:
            self.insert(num)

    def insert(self, num):
        self.tail += 1 # increment 1 before use tail
        self.heap[self.tail] = num
        cur = self.tail
        parent = int(cur/2)
        while parent > 0 and self.heap[parent] < self.heap[cur]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[cur]
            self.heap[cur] = tmp
            cur = parent
            parent = int(cur/2)

    def pop_min(self):
        # print(self.heap, end='=')
        ret = self.heap[1]
        self.heap[1] = self.heap[self.tail]
        self.tail -= 1
        # print(self.heap, self.tail+1, end='=')
        head = 1
        left = int(2*head) if int(2*head) <= self.tail else None
        right = int(2*head+1) if int(2*head+1) <= self.tail else None
        if left is not None and right is not None:
            next = left if self.heap[left]>self.heap[right] else right
        else:
            next = left if left else right
            if not next:
                return ret
        while next <= self.tail and self.heap[next] > self.heap[head]:
            tmp = self.heap[head]
            self.heap[head] = self.heap[next]
            self.heap[next] = tmp
            head = next
            left = int(2*head) if int(2*head) <= self.tail else None
            right = int(2*head+1) if int(2*head+1) <= self.tail else None
            if left is not None and right is not None:
                next = left if self.heap[left]>self.heap[right] else right
            else:
                next = left if left else right
                if not next:
                    break
        # print(self.heap)
        return ret


t = Solution()
inputs = [3,2,3,1,2,4,5,5,1]
inputs = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
print(len(inputs))

ret = t.findKthLargest(inputs, 27)
print(ret)
