# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        cur = head
        # copy all duplicated node to a hashtable
        look_up = dict()
        look_up[None] = None
        while cur:
            new = RandomListNode(cur.label)
            look_up[cur] = new
            cur = cur.next
        cur = head
        copied_head = look_up[head]
        # another run
        while cur:
            copied_head.next = look_up[cur.next]
            copied_head.random = look_up[cur.random]
            copied_head = copied_head.next
            cur = cur.next
        return look_up[head]