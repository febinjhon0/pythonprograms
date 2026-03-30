'''Hot Air Balloon Capacity Problem
A hot air balloon has a maximum weight capacity of x.
You are given:
An array s[] of size n, where each element represents the weight of a person.
Task
Select and include the maximum number of people in the hot air balloon such that:
The total weight does not exceed x.
Approach Hint
Sort the array in ascending order
Start adding people with the smallest weights first
Stop when adding another person would exceed the capacity'''

x=int(input("Enter the capacity:"))
n=int(input("Enter the numbe of people:"))
arr=[]

for i in range(1,n+1):
    w=int(input(f"Enter the weight of the {i} person:"))
    arr.append(w)
arr.sort()
total=0
count=0
for i in arr:
    if total + i <= x:
        total=total+i
        count=count+1
    else:
        break
print("Maximum people :",count)