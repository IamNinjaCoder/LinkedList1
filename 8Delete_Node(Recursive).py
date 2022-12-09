# # # Given a singly linked list of integers and position 'i', delete the node present at the 'i-th' position in the linked list recursively.

# Note :
# Assume that the Indexing for the linked list always starts from 0.

# No need to print the list, it has already been taken care. Only return the new head to the list.

from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

# Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# same as iteratively we did but here we have to do this using recursion
def deleteNodeRec(head, pos):
    if head is None:  # again the base case if head is None then just return head only
        return head
    # recurisve 2nd base case
    # pos if 0 then return the head next value only
    if pos == 0:
        return head.next
    # so this is working same as iterative method after deleting the elemnet what we will do whatever ele will be return from line 27 we just add it to the head.next like
    # 2.next=delteNodeRec(3.next,1-1)  now this recursive call will return 4 means 2.next=4 and after this we just return head which is 2-4-5 now 1.next=delenoderec(2.next,2-1)
    # 1.next=2-4-5 as 1 - 2 - 4 - 5
    head.next = deleteNodeRec(head.next, pos-1)
    return head


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    pos = int(stdin.readline().rstrip())

    newHead = deleteNodeRec(head, pos)
    printLinkedList(newHead)

    t -= 1
