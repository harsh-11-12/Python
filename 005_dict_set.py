marks = {
    "Harsh": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harsh"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Harsh": 99, "Renuka": 100})
print(marks)

print(marks.get("Harsh2")) # Prints None  when not in dict
print(marks["Harsh"]) # Returns an error when not in dict

#sets
e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 

print(s)

s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))