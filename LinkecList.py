
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 



class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            print(f"Inserted {data} at beginning")
            return 
        
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node
        print(f"Inserted {data} at end")

    def display(self):
        if not self.head:
            print("Linked list is empty")
            return
        current = self.head
        while current:
            print(f"{current.data} --> ",end="")
            current = current.next
        print("None")

    def search(self, element):
        if not self.head:
            print("Linked list is empty")
            return 
        current = self.head
        while current:
            if current.data == element:
                print("Element is present in the Linked list")
                return
            current = current.next
        print("Element not found")
        
    
    def show_class(self):
        print("\n--ENTER YOUR CHOICE--")
        print("1 -- Insert element")
        print("2 -- Display ")
        print("3 -- Search Element")
        print("4 -- Exit")
        

ll = LinkedList()
ll.show_class()
while ll.show_class:
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        data = int(input("Enter the elemnt to be inserted:"))
        ll.insert_at_end(data)

    if choice == 2:
        ll.display()

    if choice == 3:
        elem= int(input("Enter the element to be searched:"))
        ll.search(elem)

    if choice == 4:
        print("you have eexited sucesfully")
        break



# ll.display()
# ll.insert_at_end(3)
# ll.insert_at_end(4)
# ll.insert_at_end(34)
# ll.insert_at_end(36)
# ll.insert_at_end(12)
# ll.display()