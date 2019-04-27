# section 14
print('hello \n world')
print('hello \nworld')
print('hello \tworld')
print(len('hello'))
print(len('I am'))

# Section 15
mystring = "Hello World"
print(mystring)
print(mystring[8])
print(mystring[-1])

mystring = 'abcdefgijk'
print(mystring[2])
# 2: is getting values from index 2 to value the end
print(mystring[2:])
# :3 is getting values up to index 3( not including 3)
print(mystring[:3])

# getting values between index number 
print(mystring[3:6])
print(mystring[1:3])

# print everything 
print(mystring[::])

# string slicing
print(mystring[::3])
print(mystring[2:7:2])
# reverse string
print(mystring[::-1])

# SECTION 16
# IMMUTABILITY
name = "Sam"
# name[0] = 'P

last_letters = name[1:]
string_concatenation = 'P'+ last_letters
print(string_concatenation)

x ='Hello World'
print(x.upper())
print(x.split())
print(x.split('l'))









