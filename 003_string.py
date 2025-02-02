name="harsh chandra"
lastname="Pant"

print(name[0:5]) #starting from 0 to all the way till 5 excluding 5
print(name[0::2])

print(len(name))
print(name.endswith("dra"))
print(name.startswith("Ha"))
print(name.capitalize())

name1=input("Enter your name:")

print(f"Good afternoon {name1} Its a great day")

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harsh").replace("<|Date|", "24 September 2050"))

