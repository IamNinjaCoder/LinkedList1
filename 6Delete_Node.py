# You have been given a linked list of integers. Your task is to write a function that deletes a node from a given position, 'POS'.
# Note :
# Assume that the Indexing for the linked list always starts from 0.

# If the position is greater than or equal to the length of the linked list, you should return the same linked list without any change.

from sys import stdin

# Following is the Node class already written for the Linked List.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# this function will return the length of linked list which had been already explained (4Length_linkedlist)
def length(head):
    if head is None:
        return 0
    count = 0
    while head.next is not None:
        count += 1
        head = head.next
    return count


# so basically we have given a pos in the linkedlist and whatever element present at the pos we have to delete
def deleteNode(head, pos):

    # if user gives the pos less than 0 means a negative integer value or pos is greater than the length of the linked list then we should just return head as the ele is not present
    # at this pos
    # these three if condition are the if cases before doing all of the operations first check these conditions are they True or Not
    if pos < 0 or pos > (length(head)):
        return head

    # if user gives empty head or None then we should return head only not possible to remove element from the empty linkedlist

    if head is None:
        return head

    # if we have given head then the next condition we will check is the pos==0 if True then we know we have to remove or delete the head after removing the head the just next one
    # ele will now become head
    if pos == 0:
        return head.next

    # before deleting any element we need two pointers the reason for this because we want to track the prev element and if we don;t have the prev element and if we remove the ele
    # then we will lose the rest of the linkedlist after the given pos suppose 1 2 3 4 5 and we have given pos==2 now we have to delete ele 3 if we remove the ele then we will have
    # only 1 2 as a linked list and the other will gone so for this we will use prev that will just one point back to the curr in that case our prev will 2 and curr will 3 if we remove 3 we will maintain
    # a link between 2.next to 3.next
    c = 0
    prev = None
    curr = head
    while c < pos:  # this will loop work until the condition is true so for the above eg this loop will run two times c=0,1 prev will be 2 and curr will be 3
        prev = curr
        curr = curr.next
        c += 1

    # we check is prev is not None as we don;t want we get Nonetype error so just check before proceeding
    if prev is not None:  # as the condition is True prev is 2 that is not none we will enter inside this condition and maintain a link between 2.next to 3.next now 2 will point to 4
        prev.next = curr.next  # not 3
    return head  # and at the end return the updated linked list


# Taking Input Using Fast I/O.
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


# To print the linked list.
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0:

    head = takeInput()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1
