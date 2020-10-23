lst1 = []
lst2 = []
num1 = int(input("Enter the Number of elements for the List 1: "))

for i in range(num1):
    elem = int(input("Enter the list element: "))
    lst1.append(elem)

print("First List Elements are: ",lst1)

num2 = int(input("Enter the Number of elements for the List 2: "))

for i in range(num2):
    elem = int(input("Enter the list element: "))
    lst2.append(elem)

print("Second List Elements are: ",lst2)
lst3 = lst1 + lst2
print("Merged List is ", lst3)
lst3.sort()
print("Sorted List is ",lst3)
