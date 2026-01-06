class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(newNode):
    temp = newNode
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("None\nList is printed")

def length_of_List(newNode):
    temp = newNode
    count = 0
    while temp:
        count+=1
        temp = temp.next
    return count


newNode = Node(10)
newNode_1 = Node(20)
newNode_2 = Node(30)

newNode.next = newNode_1
newNode_1.next = newNode_2

printList(newNode=newNode)
print("\nlength of list : ",length_of_List(newNode))
