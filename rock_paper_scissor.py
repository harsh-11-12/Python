'''
1=rock
2=paper
3=scissor'''

import random

computer=random.choice([1,2,3])
youstr=input("Enter Your choice as 'r' ,'p' ,'s' for rock paper and scissor:")
youdict={"r":1,"p":2,"s":3}
reversedict={1:"rock",2:"paper",3:"scissor"}
you=youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(computer==you):
    print("Its a draw!!")
else:
    if(computer==1 and you==2 ):
        print("You won")
    elif(computer==1 and you==3 ):
        print("Computer won")
    elif(computer==2 and you==3 ):
        print("You won")
    elif(computer==2 and you==1 ):
        print("Computer won")
    elif(computer==3 and you==1 ):
        print("You won")
    elif(computer==3 and you==2 ):
        print("Computer won")
    else:
        print("Something went wrong")