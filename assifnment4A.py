# Binary Tree implementation
# Performing Inorder, Preorder and Postorder traversal


# Creating a Node class
class Node:

    # Constructor for creating a tree node
    def __init__(self, data):

        # Store the data
        self.data = data

        # Initially left child is empty
        self.left = None

        # Initially right child is empty
        self.right = None


# Function for Inorder traversal
def inorder(root):

    # Checking if the current node exists
    if root is not None:

        # First visit the left subtree
        inorder(root.left)

        # Then print the root node
        print(root.data, end=" ")

        # Finally visit the right subtree
        inorder(root.right)


# Function for Preorder traversal
def preorder(root):

    # Checking if node exists
    if root is not None:

        # First print the root
        print(root.data, end=" ")

        # Then visit the left subtree
        preorder(root.left)

        # Then visit the right subtree
        preorder(root.right)


# Function for Postorder traversal
def postorder(root):

    # Checking if node exists
    if root is not None:

        # First visit the left subtree
        postorder(root.left)

        # Then visit the right subtree
        postorder(root.right)

        # Finally print the root
        print(root.data, end=" ")


# Creating the root node
root = Node(1)

# Creating the left and right children
root.left = Node(2)
root.right = Node(3)

# Creating children of node 2
root.left.left = Node(4)
root.left.right = Node(5)

# Creating children of node 3
root.right.left = Node(6)
root.right.right = Node(7)


# Performing Inorder traversal
print("Inorder Traversal:")
inorder(root)

# Moving to next line
print()

# Performing Preorder traversal
print("Preorder Traversal:")
preorder(root)

print()

# Performing Postorder traversal
print("Postorder Traversal:")
postorder(root)

print()
