class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next

def increment(head):
     temp = head
     while temp is not None:
        temp.data +=1
        temp = temp.next



node1 = Node(10)
node2 = Node(20)
node1.next = node2   #10 20
increment(node1) #  this function increment the nodes value till the Node value not becomes None so first Node will become 11 and second node will be 2 after this node will be None and it will return from there
printLL(node1) #Now the value is changed Node1=11 and Node2=21 so the final ans will be 11