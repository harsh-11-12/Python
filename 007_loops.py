#while loops
l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1

# for loop
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)
else:
    print("done") # this is printed when the loop exhausts!
    
#####################################################
for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    if(i == 51):
        break # Exit the loop right now
    print(i)

#####################################################


for i in range(2):
    pass #this for loop is skipped

i = 0
while(i<2):
    print(i)
    i += 1

