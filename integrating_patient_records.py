class ListNode:
    def __init__(self, ssn, age, name):
        self.ssn = ssn
        self.age = age
        self.name = name
        self.next = None

def merge_lists(head1, head2):
    dummy = ListNode(None, None, None)
    current = dummy

    while head1 and head2:
        if head1.ssn < head2.ssn:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    
    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return dummy.next

#Patient records
patient1 = ListNode("111-11-1111", 25, "Johnny")
patient2 = ListNode("222-22-2222", 45, "Jimmy")
patient3 = ListNode("444-44-4444", 50, "Heather")

#construct linked lists
head1 = patient1
patient1.next = patient3
head2 = patient2

#merge lists
merged_head = merge_lists(head1, head2)

#print merged lists
current = merged_head
while current:
    print(f"SSN: {current.ssn}, Age: {current.age}, Name: {current.name}")
    current = current.next