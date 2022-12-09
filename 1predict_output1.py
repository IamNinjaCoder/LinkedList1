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
node2.next = node1
printLL(node2)

# Explanation ::: first Class Node is created and after then we are defining a function which will use to print the linkedlist 
#line 13 for creating the first node which is equal to 10 A node is something like which contains the data and the linking part which is called as Next when we link one node to 
#the other node then the value of .next is assigned as the address of the other Node 
#we created two nodes the second Node which is 20 now after creating this Node the next is None till now as we make a link between the node2--> node1 the value of Next becomes
#the address of node1 so node2 "Next" will have the address of node1 in this way we get the a linked list 20-->10

