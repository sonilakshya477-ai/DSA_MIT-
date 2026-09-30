# Binary Tree for Library Catalog Navigation


# Creating a node for the binary tree
class Node:

    def __init__(self, data):

        # Store category/book name
        self.data = data

        # Left child initially empty
        self.left = None

        # Right child initially empty
        self.right = None


# Function for inorder traversal
def inorder(root):

    # If node exists
    if root is not None:

        # Visit left side
        inorder(root.left)

        # Display current category
        print(root.data)

        # Visit right side
        inorder(root.right)


# Creating the main library category
root = Node("Library")

# Adding categories
root.left = Node("Computer Science")
root.right = Node("Mechanical Engineering")

# Adding subcategories
root.left.left = Node("Programming")
root.left.right = Node("Data Structures")

root.right.left = Node("Thermodynamics")
root.right.right = Node("Machine Design")


# Displaying the library catalog
print("Library Catalog:")
inorder(root)
