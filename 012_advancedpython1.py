 #using walrus operator 
if(n := len([10,78,45,12,96]))>3:
    print(f"list is too long, {n} elements, expected<=3")
 


from typing import List, Union, Tuple 

n : int = 5

def  sum(a: int, b: int) -> int:
    return a+b
print(sum(45,78))



def http_status(status): 
    match status:  
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status"  


print(http_status(5007))




dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) # Output: {'a': 1, 'b': 3, 'c': 4}


def funt():
    try:
        a=int(input("Enter only a number:"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    else:
        print("This line is executed when right input is entered as a remark, else not")
    finally:    
        print("This line is executed even you enter a wrong input or a right input, the code would carry on even after the function had returned something!")
funt()



a=int(input("Enter a number:"))
b=int(input("Enter another number:"))

if b== 0:
    raise ZeroDivisionError("Hey our program is not meant to perform division by 0")
else:
    print(f"division of two numbers is: {a/b}")




from module import myFunc




l = [3, 513, 53, 535]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")


    
myList = [1, 2, 9, 5, 3, 5]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

squaredList = [i*i for i in myList]

print(squaredList)


