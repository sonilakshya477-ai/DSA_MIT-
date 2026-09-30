# Queue implementation for a ticket booking counter

# Creating an empty list to store customers
queue = []

# Function to add a customer to the queue
def enqueue(customer):
    # append() adds the customer at the end
    queue.append(customer)
    print(customer, "joined the ticket queue.")


# Function to serve the first customer
def dequeue():
    # Checking whether the queue is empty
    if len(queue) == 0:
        print("Queue is empty. No customer to serve.")
    else:
        # pop(0) removes the first customer
        customer = queue.pop(0)
        print(customer, "has been served.")


# Function to display the queue
def display_queue():
    # Checking if the queue has no customers
    if len(queue) == 0:
        print("Queue is empty.")
    else:
        print("\nCustomers in the queue:")

        # Traversing through the queue
        for customer in queue:
            print(customer)


# Adding customers
enqueue("Rahul")
enqueue("Aman")
enqueue("Rohit")
enqueue("Karan")

# Displaying the current queue
display_queue()

# Serving the first customer
print("\nServing customer:")
dequeue()

# Displaying the queue after serving
print("\nQueue after serving one customer:")
display_queue()
