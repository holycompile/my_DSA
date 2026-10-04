#formal linked list creation

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


print("------------Normal Linked list:-----------")
#traversing

head = n1 # the n1 address basically
current = head 

while current.next!=None:
    print(current.data)
    current=current.next
print(current.data,current.next)
   
print("------------------------------------")

#n2 has the 2nd address basically

head=n2
print("After deletion from beginning:")
current = head 

while current.next!=None:
    print(current.data)
    current=current.next
print(current.data,current.next)
print("------------------------------------")


    
    