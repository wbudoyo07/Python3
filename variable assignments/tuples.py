# Tuples are very similar to lists. However they have one key difference - immutability.
# once an selement is inside a tuple, it can not be reassigned.
# Tuples use parenthesis: (1,2,3)

t = (1,2,3)

mylist = [1,2,3]
print(type(t))
print(type(mylist))
t = ('a', 'a','b')
print(t.count('a'))
print(t.index('a'))

# Immubility
mylist = [1,2,3]
mylist[0]= 'NEW VALUES'
print(mylist)
t[0] ='NEW VALUES'
