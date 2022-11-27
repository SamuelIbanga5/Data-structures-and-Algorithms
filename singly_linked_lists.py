# Node class
class Node:
    def __init__(self, data):
        self.data = data    # Assign data
        self.next = None    # Initialize next pointer to None.


# Linked List
class LinkedList:
    # Function to initialize the linked list
    # List object
    def __init__(self):
        self.head = None

    # Function to count number nodes in Linked List
    def count(self):
        temp = self.head
        count = 0
        while (temp != None):
            count += 1
            temp = temp.next
        return count

    # Function to print contents of a linked list
    # Starting with head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    # Function to insert new node in front of linked list
    def push(self, new_data):
        new_node = Node(new_data)   # Creating the new Node
        new_node.next = self.head   # Initializing next pointer of new Node to head data
        self.head = new_node    # Pointing head to new Node

    # Inserting new Node after the given previous Node
    def insertAfter(self, prev_node, new_data):
        # Check if previous node is None or if it exists.
        if prev_node == None:
            print("The given previous node must be in LinkedList.")
            return
        
        # Create new Node using new data
        new_node = Node(new_data)

        # Link new Node to the next node of previous node
        new_node.next = prev_node.next

        # Link next of previous node to the new Node
        prev_node.next = new_node

    # Function to insert new Node after the last Node/at the end.
    def append(self, new_data):
        # Creating a new Node with new_data
        new_node = Node(new_data)

        # Checking is head Node is None
        if self.head == None:
            self.head = new_node
            return
        
        # Store last Node in variable
        last = self.head
        # Traversing linked list to get last node
        while (last.next):
            last = last.next

        # Linked next pointer of last Node to new Node
        last.next = new_node

    # Function to delete a node in a particular position
    def deleteNode(self, key, position = None):
        temp = self.head
        count = 0
        # Checking if Node is not None
        if temp != None:
            # Checking if Node is first
            # Deleting the first Node of the linked list
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted in a given position and keeping track of the previous Node
        # Deleting Node in middle of Linked List
        while (temp != None):
            if (position != None):
                count += 1
                if (count - 1 == position):
                    if (temp.data == key):
                        break
            else:
                if (temp.data == key):
                    break
            prev = temp
            temp = temp.next

        # Checking if Node does not exist
        if (temp == None):
            return

        prev.next = temp.next
        temp = None

    # Function to delete from a particular index position in a Doubly Linked List
    def deleteFromPosition(self, position):
        # Assigning head Node to temp
        temp = self.head
        # Initializing index with 0
        index = 0

        # Checking if Node is not None
        if temp != None:
            # Checking if Node is first
            # Deleting the first Node of the linked list
            if position == 0:
                self.head = temp.next
                temp = None
                return
        # Checking if temp is not None
        while (temp != None):
            # Checking if index is equal to position
            if (index == position):
                break
            prev = temp
            temp = temp.next
            index += 1

        # Checking if Node exists in Linked List
        if (temp == None):
            return

        # Assigning next of current node to the next of previous Node
        prev.next = temp.next
        temp = None

# CONSTRUCTING A SIMPLE LINKED LIST
if __name__ == "__main__":
    
    # Starting with an empty list
    llist = LinkedList()

    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second    # Linking first node to second

    # second.next = third # Linking second node to third

    llist.append(4)
    llist.push(3)
    llist.push(33)
    llist.push(1)
    llist.append(5)
    llist.append(6)
    llist.append(7)
    llist.append(8)
    llist.append(3)
    llist.insertAfter(llist.head, 2)

    print(f"Number of nodes: {llist.count()}")
    print("Created linked list is: ")
    llist.printList()
    llist.deleteNode(1)
    llist.deleteNode(7)
    llist.deleteNode(5)
    llist.deleteFromPosition(0)
    llist.deleteFromPosition(1)
    
    print("Created linked list is: ")
    llist.printList()
    print(f"Number of nodes: {llist.count()}")