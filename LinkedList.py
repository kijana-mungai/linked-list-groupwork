from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index = index + 1

        if current is None:
            print("Position out of bounds")
            return
        
        new_node.next = current.next
        current.next = new_node
    
    def delete_at_position(self, position):
        if self.head is None:
            print("The list is empty")
            return
        
        if position == 0:
            self.head = self.head.next
            return
        
        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index = index + 1

        if current is None or current.next is None:
            print("Position is out of bounds")
            return
        
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")