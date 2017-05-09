class Node(object):
    def __init__(self, key=None, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity=10):
        self.capacity = capacity
        # head for O(1) insertion
        self.head = Node(0,0)
        # tail for O(1) deletion
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head
        # map for O(1) get, put
        self.map = {}
        self.count = 0

    def delete_node(self, key):
        if key not in self.map:
            return
        this = self.map[key]
        this.next.pre = this.pre
        this.pre.next = this.next

    def add_to_head(self, node):
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node

    def put(self, key, value):
        if key in self.map:
            this = self.map[key]
            self.delete_node(key)
            this.val = value
            self.add_to_head(this)
            return
        new = Node(key, value)
        self.map[key] = new
        if self.count >= self.capacity:
            # remove from hashmap
            # print(self.tail.pre.key)
            buf = self.tail.pre.key
            self.map.pop(self.tail.pre.key, None)
            # remove tail
            # print(self.tail.pre.pre.key, self.tail.pre.key)
            # todo @charles fix this, the delete_node doesn't work
            # self.delete_node(buf)
            self.tail.pre = self.tail.pre.pre
            self.tail.pre.next = self.tail
        else:
            self.count += 1
        # add new to head
        # print(self.map)
        self.add_to_head(new)
        return

    def get(self, key):
        if key in self.map:
            hit = self.map[key]
            # remove hit from linked list
            hit.pre.next = hit.next
            hit.next.pre = hit.pre
            # add hit to head
            hit.next = self.head.next
            hit.next.pre = hit
            self.head.next = hit
            hit.pre = self.head
            return self.map[key].val
        else:
            return -1


if __name__ == "__main__":
    test = LRUCache(2)
    test.put(2,1)
    test.put(1,1)
    test.put(2,3)
    print(test.get(2))
    test.put(4,1)
    print(test.get(2))
    test.get(1)
    test.get(2)
