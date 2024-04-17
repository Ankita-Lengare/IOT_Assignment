# Write a Python function to find the maximum of three numbers.

def maximum(num1, num2, num3):              #fun defination
 
    if (num1 >= num2) and (num1 >= num3):
        print("num1 is greater")
 
    elif (num2 >= num1) and (num2 >= num3):
        print("num2 is greater")
 
        
    else:
        print("num3 is greater")

n1=int(input("enter no.1= "))
n2=int(input("enter no.2= "))
n3=int(input("enter no.3= "))

maximum(n1,n2,n3)   #function call