# Student Admission Record Management using BST


# Creating a node for storing student information
class StudentNode:

    def __init__(self, admission_no, name):

        # Store the admission number
        self.admission_no = admission_no

        # Store the student's name
        self.name = name

        # Initially left child is empty
        self.left = None

        # Initially right child is empty
        self.right = None


# Function to insert a student into BST
def insert(root, admission_no, name):

    # If tree is empty, create a new student node
    if root is None:
        return StudentNode(admission_no, name)

    # Smaller admission number goes to the left
    if admission_no < root.admission_no:

        root.left = insert(root.left, admission_no, name)

    # Greater admission number goes to the right
    elif admission_no > root.admission_no:

        root.right = insert(root.right, admission_no, name)

    # If same admission number is entered
    else:
        print("Admission number already exists.")

    # Return the root node
    return root


# Function for searching a student
def search(root, admission_no):

    # If tree is empty
    if root is None:
        return None

    # If admission number matches
    if root.admission_no == admission_no:
        return root

    # Search in left subtree
    if admission_no < root.admission_no:
        return search(root.left, admission_no)

    # Search in right subtree
    else:
        return search(root.right, admission_no)


# Function to display records in sorted order
def inorder(root):

    # Check if node exists
    if root is not None:

        # Visit left subtree
        inorder(root.left)

        # Display student information
        print(
            "Admission No:",
            root.admission_no,
            "| Name:",
            root.name
        )

        # Visit right subtree
        inorder(root.right)


# Creating an empty BST
root = None


# Adding student records
root = insert(root, 105, "Rahul")
root = insert(root, 102, "Aman")
root = insert(root, 110, "Rohit")
root = insert(root, 101, "Karan")
root = insert(root, 108, "Arjun")
root = insert(root, 115, "Vivek")


# Displaying all student records
print("Student Admission Records:")
inorder(root)


# Searching for a student
print("\nSearching for Admission Number 108:")

student = search(root, 108)

# Checking whether student was found
if student is not None:

    print("Student Found")
    print("Admission No:", student.admission_no)
    print("Name:", student.name)

else:

    print("Student not found.")
