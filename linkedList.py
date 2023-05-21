class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        if self.is_empty():
            print("Linked list is empty.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> ")
                current = current.next
            print("None")

# Create an empty linked list
my_list = LinkedList()

# Insert elements at the head
my_list.insert_at_head(3)
my_list.insert_at_head(2)
my_list.insert_at_head(1)

# Insert elements at the tail
my_list.insert_at_tail(4)
my_list.insert_at_tail(5)

# Display the linked list
my_list.display()
