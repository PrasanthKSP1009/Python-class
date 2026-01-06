class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head  = None

    # insert at End
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head =  new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node

    # insert at beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # delete a node
    def delete(self, key):
        curr = self.head

        if curr and curr.data == key:
            self.head = curr.next
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
    
        prev.next = curr.next

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False
    
    def printList(self):
        curr = self.head
        while curr:
            print(curr.data, end="->")
            curr = curr.next

        print("None")

    
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)

ll.printList()

ll.delete(30)
ll.printList()
print(ll.search(2))
print(ll.search(20))