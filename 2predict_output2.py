class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40) 
node1.next = node2
node2.next = node3
node3.next = node4
printLL(node2)


#there we created 4 Nodes and from the first node we started the linking part if we print this linked list from the first Node which is the head of the linkedlist (1) then it will
# start printing from 10 20 30 40 but while calling the printLL function we sent the linkedlist from 20 not from 10 so for this function head will be the 20 but only for this function
#orignally head is 10 so that;s why it printed like 20 30 40 