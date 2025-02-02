def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}°C")

#####################################################

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

n=int(input("enter the number:"))
print(f"Sum of first {n} natural number is :{sum(n)}")

#####################################################

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

n=int(input("enter the number:"))

pattern(n)

#####################################################

