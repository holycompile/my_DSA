# For binary Search the list shall be sorted in ascending or descending order 
# O lon(n) = Time complexity
def binary(list, target):
    left=0
    right=len(list)-1
    
    while left<=right:
        mid= (left+right) // 2
        
        if list[mid]==target:
            return "Found!!"
        elif list[mid]< target:
            left=mid+1
        else:
            right=mid-1
    return "Not there..."




list=[ 2, 3, 7, 7, 11, 15, 25]

target=int(input("Enter the target value to search: "))
result=binary(list,target)
print(result)