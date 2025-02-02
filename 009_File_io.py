
st="Harsh is a very good boy too"
f=open("file.txt","w")
f.write(st)
f.close()

f=open("file.txt","r")
data=f.read()
print(data)
f.close()

#also same but no need to close here as it closes automatically
with open("file.txt") as f:
    content=f.read()
    if("Harsh" in content):
        print("The content is speaking about Harsh")
    else:
        print("The content is not speaking about Harsh")