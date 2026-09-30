# Stack implementation for managing returned library books

# Creating an empty list to work as a stack
stack = []

# Function to add a returned book into the stack
def push_book(book):
    # append() adds the book at the top of the stack
    stack.append(book)
    print(book, "has been added to the stack.")


# Function to remove the most recently returned book
def pop_book():
    # Checking whether the stack is empty or not
    if len(stack) == 0:
        print("No books are available in the stack.")
    else:
        # pop() removes the last book from the stack
        book = stack.pop()
        print(book, "has been removed from the stack.")


# Function to display all books in the stack
def display_books():
    # Checking if there are no books
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("\nBooks currently in the stack:")

        # reversed() displays the top book first
        for book in reversed(stack):
            print(book)


# Adding returned books
push_book("Python Programming")
push_book("Data Structures")
push_book("Computer Networks")
push_book("Operating Systems")

# Displaying the books
display_books()

# Removing the last returned book
print("\nReturning the top book:")
pop_book()

# Displaying the stack again
print("\nStack after removing one book:")
display_books()
