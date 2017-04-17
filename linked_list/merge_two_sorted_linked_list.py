class Node(object):
    def __init__(self):
        self.__v = None
        self.next = None

    def next(self, Node):
        self.next = Node

    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        self.__v = v

def build_linked_list_from_list(li):
    head = Node()
    head.v = li[0]
    this = head
    for each in li[1:]:
        new = Node()
        new.v = each
        this.next = new
        this = this.next
    return head

def merge_sorted_linked_list(head1, head2):
    head = tail = Node()
    # construct a new linked list
    # always compare the current head of new list with the head of two existing lists
    # link the new list to the min (head1, head2)
    while head1 is not None and head2 is not None:
        if head1.v < head2.v:
            c = head1
            head1 = head1.next
        else:
            c = head2
            head2 = head2.next
        tail.next = c
        tail = tail.next
    # link the rest of the list
    tail.next = head1 or head2
    return head.next

l1 = [1,3,4]
l2 = [1,4,6]
head1 = build_linked_list_from_list(l1)
head2 = build_linked_list_from_list(l2)

head = merge_sorted_linked_list(head1, head2)
this = head
while this != None:
    print(this.v, end=' ')
    this = this.next