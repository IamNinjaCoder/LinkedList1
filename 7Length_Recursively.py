# Given a linked list, find and return the length of the given linked list recursively.

from sys import stdin, setrecursionlimit
setrecursionlimit(10**4)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthRecursive(head):
    # base case as head will None obviously there will no len so we just return the 0
    if head is None:
        return 0
    # otherwise we just add 1 everytime while making the recursive call and pass the head.next value to it
    return 1+lengthRecursive(head.next)

# DRY RUN ---> let 1 2 3 as the linked list head is 1 condition not true come to the recursive call again function call will made now this time head will be 2 again the base case
# not true now head will 3 base case not true this time when we will pass head.next means 3.next head will None and it will return 0  so 1+0=1 this 0 comes from None and this one is
# from 3 when head was 3 now this will return 1... 1+1(from the lenRecursive(3.next)) then 1+2(from the lenRecursive(2.next)) at the end we will return 3 as all the recursive calls done


# Note: there will be runtime error in some cases that is just because we have given large input and that's why we sort out from recursive calls by default we have given 1000 calls (1Main+999Function calls itself)
# as the size increases stack will become full so we have to increase the size of the stack using setrecursionlimit library which is defined in sysmodule  and just set the limit (10**4) and check code working fine or not
# if not then just change 4 to 5 it will work
# Taking Input Using Fast I/O
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


# To print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# Main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    ans = lengthRecursive(head)
    print(ans)
    t -= 1
