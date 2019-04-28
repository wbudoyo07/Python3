myfile = open('myfile.txt')

print(myfile.read())
# We have to reset the cursor in order to read the file again
print(myfile.read())

myfile.seek(0)

# print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

with open('myfile.txt')  as my_new_file:
    contents = my_new_file.read()

# print(contents)

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read()
# print(contents)

with open('myfile.txt', mode='a') as myfile:
    contents = myfile.write("\nNEXT LINES")

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read()
print(contents)

with open('asdasdasda.txt', mode='w') as f:
    f.write(" I CREATED A NEW FILE!")

with open('asdasdasda.txt', mode='r') as f:
    f.read()
