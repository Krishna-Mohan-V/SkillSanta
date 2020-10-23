# Python Program to Swap the First and Last Value of a List

# Method 1
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)

lst[0], lst[-1] = lst[-1], lst[0]

print("Swapped List is ",lst)


# Method 2
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)

temp = lst[0]
lst[0] = lst[-1]
lst[-1] = temp

print("Swapped List is ",lst)
