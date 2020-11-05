#1 Rename the 'key' city to location in the following dictionary

SkillSanta_Dict = {"name":"Sachin","age":22,"salary":60000,"city":"New Delhi"}
print(SkillSanta_Dict)
SkillSanta_Dict["location"] = SkillSanta_Dict.pop("city")
print(SkillSanta_Dict)

#2 Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

lst = [11,12,54,34,76,45,98,12,34,54,76,45,76,12,11]
print("Original List: ",lst)
print("Element : occurence of each element is",end="  ")
print(dict(map(lambda occurence:(occurence,lst.count(occurence)),set(lst))))

#3 Remove duplicate from a list and create a tuple and find the minimum and maximum number

lst = [11,12,54,34,76,45,98,12,34,54,76,45,76,12,11]

print("Unique items in the list:",list(set(lst)))
print("Tuple of unique items is:",tuple(set(lst)))
print("Minimum of numbers is ",max(tuple(set(lst))))
print("Maximum of numbers is ",min(tuple(set(lst))))

#4 Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 50000

def showEmployee(name,sal=50000):
    print("Employee "+name+" Salary is: "+str(sal))

showEmployee("Eddy")
showEmployee("Christin",62000)

#5 Create 2 functions so that outer function accepts 2 parameters, inner function adds them and outer function adds 5 to the inner function

def outer_Func(a,b):
    def inner_Func(a,b):
        return a+b
    print(5 + inner_Func(a,b))

outer_Func(10,2)

#6 Recursive function to print the fibonacci series of n numbers

def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)

max_num = int(input("Enter maximum number for items in fibonacci series: "))

for i in range(max_num):
    print(fib(i), end=" ")

#7 Assign a different name to function and call it through the new name

def displayStudent(name,age):
    print("Person "+name+" age is "+str(age))

showStudent = displayStudent

showStudent("Eddy", 27)

#8 python function which takes a mobile number from the user until the user would not give you a proper mobile number

while True:
    num = (input("Enter the mobile number: "))
    if num.isdigit():
        if len(num) == 10:
            break
        else:
            print("\nEnter proper mobile number")
            continue
    else:
        print("\nEnter proper mobile number")
        continue

#9 Write a Python function that accepts a string and calculates the number of uppercase letters and lowercase letters

Sample_Str = input("Please enter any string: ")
u = l = 0
for i in Sample_Str:
    if i.isupper():
        u=u+1
    elif i.islower():
        l=l+1

print("\nNo of Uppercase characters: ",u)
print("\nNo of Lowercase characters: ",l)

#10 Write a Python function to check whether a number is perfect or not

choice = True
while choice:
    num = int(input("\nEnter any number to check whether it is perfect or not: "))
    sum = 0
    for div in range(1,num):
        if num % div == 0:
            sum+=div
    if sum == num:
        print("\nYes, you have entered a perfect number.")
    else:
        print("\nSorry, It is not a perfect number.")

    choice = (input("Would you like to try again?(y/n): "))
    if str(choice) == 'y':
        choice = True
    else:
        choice = False

