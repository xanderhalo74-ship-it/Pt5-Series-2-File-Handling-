file = open("cod.txt")
count=0
content = file.read()
colist = content.split("\n")
for i in colist:
    if i:
        count += 1
print("This is the number of lines in the file.")
print(counter)
