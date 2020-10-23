# Method 1 
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)
lst.sort()

print("Second largest Number in the List is ",lst[-2])


# Method 2
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)
lst.sort()
lst.reverse()
print("Second largest Number in the List is ",lst[1])


# Method 3
lst = []
num = int(input("Enter the Number of elements for the List: "))

for i in range(num):
    elem = int(input("Enter the list element: "))
    lst.append(elem)

print("List Elements are: ",lst)
lst.remove(max(lst))
print("Second largest Number in the List is ",max(lst))