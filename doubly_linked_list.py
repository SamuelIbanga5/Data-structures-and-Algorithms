# Node class
class Node:
    def __init__(self, next=None, prev=None, data=None):
        # Reference to next node in Doubly linked list
        self.next = next
        # Reference to previous node in doubly linked list
        self.prev = prev
        # Data stored in a node
        self.data = data

# Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a node in front of the Doubly linked list
    # Push Function
    def push(self, new_data):
        new_node = Node(data=new_data)

        # Make next of new Node to point to head Node
        new_node.next = self.head
        # Make previous of new Node point to None
        new_node.prev = None
        # Checking if head is not None
        if (self.head != None):
            # Make previous of head Node to point to new Node
            self.head.prev = new_node
        # Make head point to new Node
        self.head = new_node

    # Inserting new Node after a given previous Node
    def insertAfter(self, prev_node, new_data):
        # Check if prev_node exists in LinkedList
        if (prev_node == None):
            print("This node doesn't exist in the linked list!")
            return

        # Creating new node in Linked List
        new_node = Node(data=new_data)

        # Make next of new Node to point to the next of the previous Node
        new_node.next = prev_node.next
        # Make the next of previous Node to point to the new Node
        prev_node.next = new_node
        # Make previous of new Node to point to the previous Node
        new_node.prev = prev_node

        # Check if next of new Node is None
        if (new_node.next != None):
            # Make previous of next node of new Node to point to new Node.
            new_node.next.prev = new_node

    # Adding a new Node to end of Doubly Linked List
    def append(self, new_data):
        # Create new Node with new_data
        new_node = Node(data=new_data)
        last = self.head

        # Make next of new Node to point to None
        new_node.next = None
        # Check if Linked list is empty 
        if (self.head is None):
            # Make previous of new Node to point to None
            new_node.prev = None
            # Make head node point to new Node
            self.head = new_node
            return

        # Check if Last is not None
        while (last.next is not None):
            last = last.next

        # Make next of last Node to point to new Node
        last.next = new_node
        # Make previous of new Node to point to last
        new_node.prev = last

    def insertBefore(self, next_node, new_data):
        # Check if next Node is None then returning nothing
        if (next_node is None):
            return
        # Creating new Node with new_data
        new_node = Node(data=new_data) 
        # Make previous of new Node to point to the previous of next Node
        new_node.prev = next_node.prev
        # Make previous of next Node to point to the new Node
        next_node.prev = new_node
        # Make next of new Node to point to the next Node
        new_node.next = next_node
        # Check if is not None then make previous of new Node to point to new Node
        # Else make head to point to new Node
        if (new_node.prev is not None):
            new_node.prev.next = new_node
        else:
            self.head = new_node

    # Function to delete a Node with given key as Node data
    def deleteNode(self, key):
        # Referencing head Node with temp
        temp = self.head

        # Checking if the first Node(head Node) is equal to the key
        if (temp.data == key):
            # Make head Node to point to the next of the head Node
            self.head = temp.next
            # Make previous of the head Node to point to None
            temp.prev = None

        # Checking if temp is not None
        while (temp):
            # Checking if temp data is equal to key then terminating loop
            if (temp.data == key):
                break
            # Reassigning next pointer of temp to temp
            temp = temp.next
        
        # Checking if Node with key as data exists in Linked List
        if (temp == None):
            print(f"The Node with data {key} does not exist!")
            return

        # Checking if next of temp is not None and if previous is not None
        if (temp.next is not None and temp.prev is not None):
            # Making next pointer of the previous node of temp to point to next Node of temp
            temp.prev.next = temp.next
            # Making previous of the next Node to point to previous of temp Node
            temp.next.prev = temp.prev

    # Function to print the contents of a Doubly Linked List
    def printList(self):
        # Assigning head Node to temp
        temp = self.head
        # Checking if temp is not None
        while (temp is not None):
            # Printing temp data
            print(temp.data)
            # Reassigning next node of temp to temp
            temp = temp.next


if (__name__ == "__main__"):
    llist = DoublyLinkedList()

    llist.append(15)
    llist.append(18)
    llist.append(21)
    llist.push(12)
    llist.push(9)
    llist.push(6)
    llist.push(3)
    llist.push(0)

    print("Items in doubly linked list: ")
    llist.printList()

    print("Items in doubly linked list after adding extra elements: ")
    llist.insertAfter(llist.head, 1)
    llist.insertBefore(llist.head, 5)
    llist.deleteNode(21)
    llist.deleteNode(20)
    # llist.deleteNode(5)
    # llist.deleteNode(0)
    llist.printList()