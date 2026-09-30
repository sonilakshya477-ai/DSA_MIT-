# Binary Search Tree implementation
# Inorder and Preorder traversal without recursion


# Creating a node
class Node:

    def __init__(self, data):

        # Store the value
        self.data = data

        # Left child
        self.left = None

        # Right child
        self.right = None


# Function to insert a value into BST
def insert(root, data):

    # If tree is empty, create a new node
    if root is None:
        return Node(data)

    # If data is smaller, insert in left subtree
    if data < root.data:
        root.left = insert(root.left, data)

    # If data is greater, insert in right subtree
    elif data > root.data:
        root.right = insert(root.right, data)

    # Return the root
    return root


# Non-recursive Inorder traversal
def inorder(root):

    # Creating an empty stack
    stack = []

    # Start from root
    current = root

    print("Inorder Traversal:")

    # Continue while current exists or stack has nodes
    while current is not None or len(stack) > 0:

        # Move to the leftmost node
        while current is not None:

            # Store current node in stack
            stack.append(current)

            # Move to left child
            current = current.left

        # Take the last node from stack
        current = stack.pop()

        # Print the node
        print(current.data, end=" ")

        # Move to right child
        current = current.right

    print()


# Non-recursive Preorder traversal
def preorder(root):

    # If tree is empty
    if root is None:
        return

    # Creating a stack
    stack = [root]

    print("Preorder Traversal:")

    # Continue until stack becomes empty
    while len(stack) > 0:

        # Remove the top node
        current = stack.pop()

        # Print the node
        print(current.data, end=" ")

        # Add right child first
        if current.right is not None:
            stack.append(current.right)

        # Add left child second
        if current.left is not None:
            stack.append(current.left)

    print()


# Initially tree is empty
root = None

# Inserting values
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 60)
root = insert(root, 80)


# Performing traversals
inorder(root)
preorder(root)
