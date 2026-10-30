# Linear Search is O(n) time complexity 
def linear(list,num):
    for i in range (len(list)):
        if(list[i]==num):
            return "Found !"
    return "Not there..."
        
list=[3, 7, 2, 9, 5, 1, 8, 4, 6]

target=int(input("Enter the number you want to find: "))

result = linear(list,target)

print(result)