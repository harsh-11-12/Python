a=int(input("Enter Your age:"))

#if statement 1
if(a%2==0):
    print("You are at even age")

#if statement 2
if(a>=18):
    print("You are balik!")
elif(a<0):
    print("You are entering invalid age")
else:
    print("You are nabalik")
    
#######################################

marks1=int(input("Enter marks of subject 1:"))
marks2=int(input("Enter marks of subject 2:"))
marks3=int(input("Enter marks of subject 3:"))
marks=(marks1+marks2+marks3)/3
if(marks  >= 40.0 and marks1>33.0 and marks2>33.0 and marks3>33.0):
    print("You are pass!\n Congratulations")
else:
    print("Unfortunately you failed\n Better luck next time")