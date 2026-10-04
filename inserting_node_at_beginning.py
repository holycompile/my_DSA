#existing linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
#techiquall all the n1,n2,n3 has the adresses 
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)

n1.next=n2 
n2.next=n3
n3.next=n4

#traversing

head = n1 # the n1 address basically
current = head 

print("Current Linked List:")
print("--------------------------")
while current.next!=None:
    print(current.data)
    current=current.next
print(current.data,current.next)
print("-----------------------------")

value=int(input("Enter the Value you want to add in the 1st position:"))

#1st we are going to the 1st place that is head 
#head is already assigned

n_first=Node(value) #n_first has the new address now 

n_first.next=head # putting the head address in the next part 

print("Current Head:",head)
print("First Node now:",n_first.data,n_first.next)
head = n_first
print("Updated head: ",head)
print("--------------------------")
print("New traversal:")
print("--------------------------")
current = head 

print("Current Linked List:")
print("--------------------------")
while current.next!=None:
    print(current.data)
    current=current.next
print(current.data,current.next)
print("-----------------------------")
