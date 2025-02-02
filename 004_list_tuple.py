# list
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4]) 
print(friends)

l1=[5,8,2.9,58,1,26,4]

l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.insert(4,45)
print(l1)
l1.sort()
print(l1)
l1.pop(4)
print(l1)
l1.remove(58)
print(l1)
l1.append(111)
print(l1)



#tuples
tuple=(1,)  #singleton tu9ple
a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)

i = a.index(3424)
print(i)

print(len(a))