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
        self.head = None
        
    def append(self, order):
        if not self.head:
            self.head = Node(order)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(order)
    
    def display(self):
        current = self.head
        while current:
            print(current.order)
            current = current.next

    def reverse(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, node):