# Which starting number, under one million, produces the longest
# Collatz sequence?

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def set_val(self, val):
        self.val = val
    def get_val(self):
        return self.val
    def set_next(self, val):
        self.next = val
    def get_next(self):
        return self.next

class LinkedList(object):
    def __init__(self):
        self.head = None

    def node_list(self):
        node_list = []
        head = self.head
        while (head != None):
            node_list.append(head.get_val())
            head = head.get_next()
        return node_list

def collatz_seq(n):
    curr = Node(n)
    seq = LinkedList()
    seq.head = curr
    while (curr.get_val() != 1):
        number = curr.get_val()
        if (number % 2 == 0):
            curr.set_next(Node(number // 2))
            curr = curr.get_next()
        else:
            curr.set_next(Node(3*number + 1))
            curr = curr.get_next()
    return seq

max_i = 0
max_seq = 0
for i in range(1, 1000000):
    seq_i = collatz_seq(i)
    seq_i_length = len(seq_i.node_list())
    if (seq_i_length > max_seq):
        max_seq = seq_i_length
        max_i = i

print(max_i, max_seq)
# answer equals 837799
