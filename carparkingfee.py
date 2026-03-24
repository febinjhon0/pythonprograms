# Question
""" Car Parking Fee Calculation Problem
A parking lot charges fees based on the number of hours a vehicle is parked:
For the first 2 hours: ₹100 per hour
For 3 to 5 hours: ₹200 for the first 2 hours + ₹50 per additional hour
For more than 5 hours: ₹200 (first 2 hours) + ₹150 (next 3 hours) + ₹20 per additional hour
Task
Write a program to compute the total parking fee based on the number of hours n.
Examples 
If n = 2
→ Total = 2 × 100 = ₹200
If n = 3
→ Total = 200 + 50 = ₹250
If n = 6
→ Total = 200 + 150 + 20 = ₹370 """

#code

while(True):
    a=int(input("Enter the number of Hours:"))
    n=0
    sum=0
    if a<=2:
        for i in range(a):
            hr=100
            sum=sum+hr
        print(sum)
    elif a>=3 and a<=5:
        for i in range(2,a):
            sum=200
            n=n+50
            total=sum+n
        print(total)
    elif a>=6:
        for i in range(5,a):
            sum=350
            n=n+20
            total=sum+n
        print(total)
        
    
        
    