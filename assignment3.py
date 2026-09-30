# Singly Linked List implementation
# This program is used to manage a library book catalog


# Creating a Node class
class Node:

    # Constructor to create a new node
    def __init__(self, data):

        # Storing the book name in the node
        self.data = data

        # Initially the next node is None
        self.next = None


# Creating the Linked List class
class LinkedList:

    # Constructor of LinkedList
    def __init__(self):

        # Initially there is no first node
        self.head = None


    # Function to insert a book at the beginning
    def insert_beginning(self, data):

        # Creating a new node
        new_node = Node(data)

        # New node points to the current first node
        new_node.next = self.head

        # Making the new node the first node
        self.head = new_node

        print(data, "inserted at beginning.")


    # Function to insert a book at the end
    def insert_end(self, data):

        # Creating a new node
        new_node = Node(data)

        # If list is empty, new node becomes head
        if self.head is None:
            self.head = new_node
            print(data, "inserted at end.")
            return

        # Start from the first node
        temp = self.head

        # Move until the last node
        while temp.next is not None:
            temp = temp.next

        # Connect the last node to the new node
        temp.next = new_node

        print(data, "inserted at end.")


    # Function to delete the first book
    def delete_beginning(self):

        # Checking whether the list is empty
        if self.head is None:
            print("Library catalog is empty.")
            return

        # Store the book that is going to be deleted
        deleted_book = self.head.data

        # Move head to the second node
        self.head = self.head.next

        print(deleted_book, "deleted from beginning.")


    # Function to display all books
    def display(self):

        # Checking if list is empty
        if self.head is None:
            print("Library catalog is empty.")
            return

        # Start from the head
        temp = self.head

        print("\nLibrary Catalog:")

        # Continue until the end of the list
        while temp is not None:

            # Display the current book
            print(temp.data)

            # Move to the next node
            temp = temp.next


# Creating an object of LinkedList
library = LinkedList()

# Inserting books at beginning
library.insert_beginning("Python Programming")
library.insert_beginning("Data Structures")

# Inserting books at end
library.insert_end("Operating Systems")
library.insert_end("Computer Networks")

# Displaying the catalog
library.display()

# Deleting the first book
print("\nDeleting first book:")
library.delete_beginning()

# Displaying catalog again
library.display()
