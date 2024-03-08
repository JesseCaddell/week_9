class Order:
    def __init__(self, order_id, customer_details, order_details):
        self.order_id = order_id
        self.customer_details = customer_details
        self.order_details = order_details

    def __str__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_details}, Details: {self.order_details}"
    
class Node:
    def __init__(self, order):
        self.order = order
        self.next = None
        
    def append(self, order):
        if not self.next: #if linked list is empty
            self.next = Node(order) #create first node
        else:
            current = self.next
            while current.next:
                current = current.next
            current.next = Node(order)
    
    def display(self):
        current = self.next
        while current:
            print(current.order)
            current = current.next

    def reverse(self):
        prev = None
        current = self.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.next = prev #Update the head to point to the new first node

    def _reverse_recursive(self, prev, current):
        if not current:
            return prev
        next_node = current.next
        current.next = prev
        return self._reverse_recursive(current, next_node)
    
    def reverse_recursive(self):
        self.next = self._reverse_recursive(None, self.next) #Start recursion from the first node


# Create orders
order1 = Order(1, "Customer A", "Details A")
order2 = Order(2, "Customer B", "Details B")
order3 = Order(3, "Customer C", "Details C")

# Create linked list
linked_list = Node(None)  # Initialize with a dummy node
linked_list.append(order1)
linked_list.append(order2)
linked_list.append(order3)

# Display original list
print("Original List:")
linked_list.display()

# Reverse the linked list
linked_list.reverse()

# Display reversed list
print("\nReversed List:")
linked_list.display()