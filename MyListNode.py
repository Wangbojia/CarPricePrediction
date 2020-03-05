class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class _LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self):
        print(self.head)

    def addInHead(self, val):
        if not self.head:
            self.head = self.tail = ListNode(val)
            self.size += 1
            return self.head
        new_head = ListNode(val)
        self.head = new_head
        self.size += 1
        return self.head

    def addInTail(self, val):
        if not self.tail:
            return self.addInHead(val)
        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.size += 1
        return self.head

    def addbyIndex(self, index, val):
        if self.size < 0 or self.size >= index:
            exit(1)
        elif self.size == 0:
            pass
        elif self.size == self.size - 1:
            pass
        else:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            mynode = ListNode(val)
            mynode.next = cur.next
            cur.next = mynode
            return self.head
