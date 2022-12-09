# For a given singly linked list of integers, find and return its length. Do it using an iterative method.

from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head) :
    #Your code goes here
    if head is None:  #this the base case if head becomes None means we have no head user directly enters -1 this means the value is None so the len will be 0
        return 0

    lenll=0
    curr=head
    while curr is not None:   #this is checking condition until curr not becomes None we have to go inside this loop and increment the value of Lenll by one everytime
        lenll+=1    
        curr=curr.next   #incrementing the curr so that it can point to the next linkedlist ele 
    return lenll


####Dry Run:  Given Linked List (1--2--3--4--5) the head is 1 means first condition will not be True now lenll is zero we initialize curr=head curr is 1 
#as curr is not None we entered inside the loop and increment the value of lenll to 1 now lenll will be 1 now curr will point to the 2 again while condition is True curr is not None
#we go and do the same operations we  will do util curr not becomes none after the value of 5 curr will point to None and this time condition will become false and we just return the  lenll

#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()



#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    print(length(head))

    t -= 1