class MinHeap(object):
    def __init__(self):
        '''
        Array implementation, array index starts at 1
        given index k:
        parent node is int(k/2)
        left child is 2*k
        right child is 2*k+1
        '''
        self.heap = list()
        self.heap.append(0)

    def insert(self,x):
        self.heap.append(x)
        pos = len(self.heap)-1
        # compare this new element with its parent
        while pos > 0:
            parent = int(pos/2)
            if self.heap[pos] < self.heap[parent]:
                self.heap[pos], self.heap[parent] = self.heap[parent], self.heap[pos]
                pos = parent
            else:
                break


    def __len__(self):
        return len(self.heap[1:])

    def __repr__(self):
        return self.heap[1:]

    def __str__(self):
        return (', '.join([str(x) for x in self.heap[1:]])).join(['[', ']'])

    def getMin(self):
        if len(self.heap) == 1:
            raise Exception('Empty Heap')
        return self.heap[1]

    def percDown(self, cur):
        hl = len(self.heap)
        pos = cur
        left = pos * 2
        right = pos * 2 + 1 if pos * 2 + 1 < hl else left
        if left < hl:
            left_val, right_val = self.heap[left], self.heap[right]
            next_idx = left if left_val < right_val else right
            if self.heap[cur] > self.heap[next_idx]:
                self.heap[cur], self.heap[next_idx] = self.heap[next_idx], self.heap[cur]
                self.percDown(next_idx)

    def deleteMin(self, recursive=False):
        if len(self.heap) == 1:
            raise Exception('Empty Heap')
        # swap root and last node in tree
        self.heap[1], ret = self.heap[-1], self.heap[1]
        self.heap.pop(-1)
        pos = 1
        hl = len(self.heap)

        # recursive approach
        if recursive:
            self.percDown(1)

        else:
            # iterative approach
            while True:
                left = pos * 2
                right = pos * 2 + 1 if pos * 2 + 1 < len(self.heap) else left
                if right >= hl:
                    break
                child_idx = left if self.heap[left] < self.heap[right] else right
                if self.heap[pos] > self.heap[child_idx]:
                    self.heap[pos], self.heap[child_idx] = self.heap[child_idx], self.heap[pos]
                    pos = child_idx
                else:
                    break


        return ret

    def getHeap(self):
        return self.heap[1:]






import random
episode = 100
for _ in range(episode):
    original = [random.randint(0,100) for x in range(100)]
    # original = [0 for _ in range(10)]

    test = MinHeap()
    for x in original:
        test.insert(x)
    # sorted = [test.deleteMin() for _ in range(len(test))]
    sorted_test = []
    answer = sorted(test.getHeap())
    for _ in range(len(original)):
        sorted_test.append(test.deleteMin(recursive=True))
    if sorted_test != answer:
        raise Exception('bug',sorted_test, answer)
