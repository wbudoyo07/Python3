# Sets are unordered collections of unique elements
# Meaning there can only be one representative of the same object.

myset = set()
myset.add(1)
myset.add(2)
myset.add(2)

# sets only accept unique value
print(myset)

mylist = [1,1,1,1,2,2,2,2,3,3,3,3,3]
mylistunordered = [2,2,2,2,3,3,3,3,1,1,1,1,]

print(set(mylist))
print(set(mylistunordered))