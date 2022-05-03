'''
Given a sorted linked list and a value to insert,
write a function to insert the value in a sorted way

pseudocode:
1. If the linked list is empty, make the node as the start and make it head.
2.  If the value of the node to be inserted is smaller than the value of the head node
then insert the node in the start and make it the head
3. In a loop, find the appropriate node after which the input node is to be inserted.
To find the appropriate node, start from the head and keep moving until you reach a
node GN whose value is greater than the input node. The node just before GN is the
appropriate node
4. Insert the node after the appropriate node found in step 3

Time complexity: O(n)
Space: O(1)
'''
# Node class
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize the head
    def __init__(self):
        self.head = None

    def sortedInsert(self, new_node):
        # Special case for the empty linked list
        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            # Locate the node before the point of insertion
            current = self.head
            while ( current.next is not None and
                    current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print it the LinkedList
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Main Program
llist = LinkedList()
new_node = Node(5)
llist.sortedInsert(new_node)
new_node = Node(10)
llist.sortedInsert(new_node)
new_node = Node(7)
llist.sortedInsert(new_node)
new_node = Node(3)
llist.sortedInsert(new_node)
new_node = Node(1)
llist.sortedInsert(new_node)
new_node = Node(9)
llist.sortedInsert(new_node)

print("Create Linked List")
llist.printList()
