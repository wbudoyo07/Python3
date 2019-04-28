mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    # check for even numbers
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

mystring = 'Hello World'

for letter in mystring:
    print(letter)

# _ common syntax when you don't intend to use variable name
for _ in 'Hello World':
    print("Cool")

tup = (1,2,3)

for item in tup:
    print(item)

mylist = [(1,2),(3,4),(5,6),(7,8)]

for item in mylist:
    print(item)

# tuple unpacking
for a,b in mylist:
    print(a)
    print(b)

mylist = [(1,2,3), (5,6,7),(8,9,10)]

for a,b,c in mylist:
    print(b)


# iterate dict
d = {'k1':1, 'k2':2, 'k3':3}

for key, value in d.items():
    print(value)