# Python program to find the largest number in a list

# Method 1
lst = [] 
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)

print("Largest Number in the List is ",max(lst))


# Method 2
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)
lst.sort()

print("Largest Number in the List is ",lst[num-1])


# Method 3
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)

largest_num = lst[0]
for i in range(1,num):
    if lst[i] > largest_num:
        largest_num = lst[i]
print("Largest Number in the List is ",largest_num)

