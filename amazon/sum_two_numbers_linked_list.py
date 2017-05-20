# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current = None
        rem = 0
        stack1 = list()
        head = l1
        while head.next is not None:
            stack1.append(head.val)
            head = head.next
        while l1 or l2:
            # while len(l1) > 0 or len(l2) > 0:
            l1_buf = l1.val if l1 else 0
            l2_buf = l2.val if l2 else 0
            # this_ret = l1_buf + l2_buf + rem
            this_node = ListNode(l1_buf + l2_buf + rem)
            rem = this_node.val / 10
            this_ret = this_node.val % 10
            this_node.val = this_ret
            this_node.next = current
            if current == None:
                head = this_node
            current = this_node
            l1 = l1.next if l1.next else None
            l2 = l2.next if l2.next else None

        return head