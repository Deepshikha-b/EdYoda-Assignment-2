size = int(input("Enter the size of your list : "))
lst1 = []
lst2 = []
for i in range(size):
    data1 = int(input("Enter the element for list1 : "))
    lst1.append(data1)
    
for i in range(size):
    data2 = int(input("Enter the element for list2 : "))
    lst2.append(data2)
    
lst = list(zip(lst1,lst2))
print("Original list is :",lst)

var = 1
for i in range(size): 
    for j in range((size-i)-1): 
        if (lst[j][var] > lst[j + 1][var]):  
            temp = lst[j]  
            lst[j]= lst[j + 1]  
            lst[j + 1]= temp   
print("Sorted list is: ",lst)
