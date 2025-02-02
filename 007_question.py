n=int(input("Enter a number:"))
i=1
for i in range(11):
    print(f"{n} x {i} = {n*i}")

l = ["Harsh", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

#prime number
n = int(input("Enter the number: "))
if n < 0:
    print("Enter a positive number")
elif n == 0 or n == 1:
    print("The number is not a prime number")
elif n == 2:
    print("The number is prime")
else:
    for i in range(2,n):
        if(n%i==0):
            print("number is not prime")
            break
    else:
            print("The number is prime")

 
#fact
n=int(input("Enter the number:"))
i=1
fact=1
for i in range(1,n+1):
    fact*=i
    i+=1
print(fact)
 #star
'''
  *
 ***
*****'''

n=int(input("Enter a number:"))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

'''
n=3
***
* *
***'''

n=int(input("Enter a number:"))
print("*"*n)
for i in range(1,n-1):
    print("*",end="")
    print(" "*(n-2),end="")
    print("*")
print("*"*n)

n=int(input("Enter a number:"))
i=1
for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")

