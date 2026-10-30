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

while current.next!=None:
    print(current.data)
    current=current.next
print(current.data,current.next)
   
    
    