# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        track_A = headA
        track_B = headB
        len_A = self.find_length(track_A)
        len_B = self.find_length(track_B)
        A_shorter = len_A < len_B
        diff = abs(len_A-len_B)
        track_A = headA
        track_B = headB
        if A_shorter:
            while diff:
                track_B = track_B.next
                diff -= 1
        else:
            while diff:
                track_A = track_A.next
                diff -= 1
        # share the same head
        while True:
            if track_A == track_B:
                return track_A
            if not track_A.next:
                return None
            track_A = track_A.next
            track_B = track_B.next
        return None


    def find_length(self, head):
        count = 0
        this = head
        while this.next != None:
            this = this.next
            count += 1
        return count