# For a given a singly linked list of integers and a position 'i', print the node data at the 'i-th' position.


from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None




def printIthNode(head, i):
    #Your code goes here
    if head is None:
        return 
    curr=head
    count=0
    #while curr is not none the loop will be executed and if the ith pos is greater than the len of the 
    #linked list then it will simply complete the loop and nothing will be printed
    
    while curr!=None:
        if count==i:#if count is equal to the ith node for which we want to find the element it will simply
            #print the data and returun from the loop
            print(curr.data)
        curr=curr.next #when if condition becomes fail then curr data will point to the next reference point
        
        count+=1


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
    i = int(stdin.readline().rstrip())
    printIthNode(head, i)


    t -= 1