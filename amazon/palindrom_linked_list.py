# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        stack = list()
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        while len(stack) != 0:
            cur = stack.pop()
            if head.val != cur.val:
                return False
            head = head.next

        return True



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def from_list(self, l):
        head = ListNode(None)
        cur = head
        for i in l:
            next = ListNode(i)
            cur.next = next
            cur = next
        return head.next

    def traverse(self, head):
        cur = head
        ret = []
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return ret

l = [1,2,3]
ll = ListNode.from_list(ListNode, l)
ret = ll.traverse(ll)
print(ret)
t = Solution()
ret = t.isPalindrome(ll)
print(ret)